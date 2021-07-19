class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        for i in range(len(A)):
            key=A[i]
            check=None
            for j in range(i+1,len(A)):
                if A[j]<key:
                    pass
                else:
                    check=j
                    break
            for k in range(j+1,len(A)):
                if A[k]<key:
                    return 0
        return 1
TC=O(n)
SC=O(n)
