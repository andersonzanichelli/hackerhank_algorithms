#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1:
        return 'NO'
    
    idx = 0
    a1 = x1
    a2 = x2
    
    while idx <= 10000:
        a1 = a1 + v1
        a2 = a2 + v2
        
        if a1 == a2:
            return 'YES'
        
        idx = idx + 1
    
    return 'NO'

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)