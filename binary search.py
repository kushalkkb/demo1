#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Mahesh
#
# Created:     19-05-2023
# Copyright:   (c) Mahesh 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time

start = time.time()

def binary_search(arr, l, h, x):
    if h >= l:
        m = (h + l) // 2
        if arr[m] == x:
            return m
        elif arr[m] > x:
            return binary_search(arr, l, m - 1, x)
        else:
            return binary_search(arr, m + 1, h, x)
    else:
        return -1

arr = [2,4,10,22,40]
x = 4

result = binary_search(arr, 0, len(arr) - 1, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

end = time.time()

print("Running time of the program is", end - start)
