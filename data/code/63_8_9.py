import sys

def reverse_integer(x: int) -> int:
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    
    if x == 0:
        return 0
        
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_x = 0
    
    while x != 0:
        digit = x % 10
        x = x // 10
        
        if reversed_x > INT_MAX // 10 or (reversed_x == INT_MAX // 10 and digit > 7):
            return 0
        if reversed_x < INT_MIN // 10 or (reversed_x == INT_MIN // 10 and digit < -8):
            return 0
            
        reversed_x = reversed_x * 10 + digit
        
    return sign * reversed_x

if __name__ == '__main__':
    test_values = [123, -123, 1534236469, 0, -2147483648, 1563847412]
    for val in test_values:
        result = reverse_integer(val)
        print(result)