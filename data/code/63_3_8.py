import sys

def reverse_integer(x):
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    negative = x < 0
    x = abs(x)
    reversed_x = 0
    
    while x != 0:
        digit = x % 10
        x //= 10
        
        if reversed_x > (INT_MAX - digit) // 10:
            return 0
        
        reversed_x = reversed_x * 10 + digit
    
    if negative:
        reversed_x = -reversed_x
    
    if reversed_x < INT_MIN or reversed_x > INT_MAX:
        return 0
    
    return reversed_x

if __name__ == '__main__':
    sample_inputs = [123, -123, 120, 0, 1534236469, -2147483648, 2147483647, -1563847412]
    for value in sample_inputs:
        result = reverse_integer(value)
        print(result)