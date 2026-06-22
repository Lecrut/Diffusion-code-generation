import math

def reverse_integer(x: int) -> int:
    reversed_val = 0
    sign = 1 if x >= 0 else -1
    num = abs(x)
    
    while num > 0:
        digit = num % 10
        reversed_val = reversed_val * 10 + digit
        num = num // 10
        
    reversed_val *= sign
    
    if reversed_val < -(2 ** 31) or reversed_val > (2 ** 31 - 1):
        return 0
        
    return reversed_val

if __name__ == '__main__':
    samples = [123, -123, 120, 0, 1534236469, -2147483648]
    for s in samples:
        print(reverse_integer(s))