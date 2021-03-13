def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        count = 0
        
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            count += 1
        
        print("Iteration:", count, "-", arr)

insertion_sort([10,8,6,4,2,0,9,7,5,3,1])