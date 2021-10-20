arr = [2,1,34,6,5,2]

def selection_sort(arr):
  n = len(arr)
  for i in range(0,n-1):
    minpos = i
    for j in range(i,n):
      if arr[minpos] > arr[j]:
        minpos = j

    arr[i], arr[minpos] = arr[minpos], arr[i]

  return arr

print(selection_sort(arr)) 
