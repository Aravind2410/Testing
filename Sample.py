def gre(arr,n):
    max_sum = float('-inf')
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum       


n = int(input("Size: "))
arr = list(map(int,input("Enter: ").split()))
print("the ans is: ",gre(arr,n))
