import copy
class Solution:
    """
    TC:O(2^(m+n)); m - target, n - number of choices
    AS:O(2^(m+n)); m - target, n - number of choices
    """
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        For Loop: Backtracking
        """
        result = []
        
        def helper(candidates, pivot, target, path):

            # base logic
            if target == 0:
                result.append(copy.deepcopy(path))
                return
            if target < 0:
                return

            # logic
            # Running for loop at each node from pivot to remaining nodes
            for i in range(pivot, len(candidates)):
                path.append(candidates[i])
                helper(candidates, i, target-candidates[i], path) # pivot till end of the list

                # backtrack
                path.pop()

        helper(candidates, 0, target, []) 
        return result 


    def combinationSum1(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        For Loop : Deepcopy
        TC:O(2^(m+n)); m - target, n - number of choices
        AS:O(2^(m+n)); m - target, n - number of choices
        """
        result = []
        
        def helper(candidates, pivot, target, path):

            # base logic
            if target == 0:
                result.append(copy.deepcopy(path))
                return
            if target < 0:                              
                return

            # logic
            # Running for loop at each node from pivot to remaining nodes
            for i in range(pivot, len(candidates)):
                li = []
                li = copy.deepcopy(path)
                li.append(candidates[i])
                helper(candidates, i, target-candidates[i], li) # pivot till end of the list

        helper(candidates, 0, target, []) 
        return result 


    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        0-1 Matrix : Backtrack
        TC:O(2^(m+n)); m - target, n - number of choices
        AS:O(2^(m+n)); m - target, n - number of choices
        """
        result = []
        
        def helper(candidates, idx, target, path):

            if target == 0:
                result.append(copy.deepcopy(path))
                return

            # base logic
            if idx == len(candidates) or target < 0:
                return

            # not choose -> deepcopy at each and every step
            helper(candidates, idx+1, target, path)

            # choose -> deepcopy at each and every step
            path.append(candidates[idx])
            helper(candidates, idx, target - candidates[idx ], path)

            #backtrack
            path.pop()

        helper(candidates, 0, target, []) 
        return result  


    # Just slow because of the Deepcopy at each and every step
    def combinationSum3(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        0-1 Matrix : Deepcopy

        Not choose
        Choose
        Deepcopy

        TC:O(2^(m+n)); m - target, n - number of choices
        AS:O(2^(m+n)); m - target, n - number of choices
        """
        result = []
        
        def helper(candidates, idx, target, path):

            if target == 0:
                result.append(path)
                return

            # base logic
            if idx == len(candidates) or target < 0:
                return

            # not choose -> deepcopy at each and every step
            helper(candidates, idx+1, target, copy.deepcopy(path))

            # choose -> deepcopy at each and every step
            path.append(candidates[idx])
            helper(candidates, idx, target - candidates[idx ], copy.deepcopy(path))

        helper(candidates, 0, target, []) 
        return result   
        

    def combinationSum4(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        0-1 Matrix : Deepcopy

        Choose
        Not choose
        Deepcopy
        
        TC:O(2^(m+n)); m - target, n - number of choices
        AS:O(2^(m+n)); m - target, n - number of choices
        """
        result = []
        
        def helper(candidates, idx, target, path):

            if target == 0:
                result.append(path)
                return

            # base logic
            if idx == len(candidates) or target < 0:
                return

            # choose -> deepcopy at each and every step
            li = copy.deepcopy(path)
            li.append(candidates[idx])
            helper(candidates, idx, target - candidates[idx ], li)

            # not choose -> deepcopy at each and every step
            helper(candidates, idx+1, target, copy.deepcopy(path))
 
        helper(candidates, 0, target, []) 
        return result  
