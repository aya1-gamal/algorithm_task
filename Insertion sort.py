def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        x = i-1
        while x >=0 and key < arr[x] :
                arr[x+1] = arr[x]
                x -= 1
        arr[x+1] = key


arr = [10, 15, 20, 16, 80, 100, 0,1200]
insertion_sort(arr)
print(arr)