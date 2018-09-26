# First approach
def inRange(arr, last):
  newRange = []
  if (last[0] <= arr[0]):
    if (last[1] >= arr[0]):
      newRange.append(last[0])
      newRange.append(max(last[1], arr[1]))
      return newRange
  return False

def merge(arr):
  merged = []
  arr.sort()
  for i, r in enumerate(arr):
    if (i == 0):
      merged.append(arr[i])
    else:
      lenMerged = len(merged)
      lastRange = merged[lenMerged - 1]
      newR = inRange(arr[i], lastRange)
      if (newR == False):
        newR = inRange(lastRange, arr[i])
      if (newR == False):
        merged.append(arr[i])
      else:
        merged.pop(-1)        
        merged.append(newR)
  print(merged)
