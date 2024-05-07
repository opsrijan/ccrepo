def solve(n,arr):
    if n==0:
        return 0
    elif n<0:
        return 10**9
    if n in arr:
        return arr[n]
    else:
        arr[n]=1+min(solve(n-15,arr),solve(n-10,arr),solve(n-6,arr),solve(n-3,arr),solve(n-1,arr))
        return arr[n]
    
arr=[0 for i in range(1111111)]
solve(100000,arr)