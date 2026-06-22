def reverse_integer(n: int) -> int:
    sign = -1 if n < 0 else 1
    abs_n = abs(n)
    reversed_str = str(abs_n)[::-1]
    reversed_val = int(reversed_str) * sign
    
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    if reversed_val > INT_MAX or reversed_val < INT_MIN:
        return 0
    
    return reversed_val

if __name__ == '__main__':
    result1 = reverse_integer(123)
    print(result1)
    
    result2 = reverse_integer(-456)
    print(result2)
    
    result3 = reverse_integer(120)
    print(result3)
    
    result4 = reverse_integer(1534236469)
    print(result4)