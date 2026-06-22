def reverse_integer(x: int) -> int:
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    result = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    while x != 0:
        digit = x % 10
        if result > (INT_MAX - digit) // 10:
            return 0
        result = result * 10 + digit
        x //= 10
    
    return result * sign

if __name__ == '__main__':
    test_values = [123, -456, 120, 0, 1534236469]
    for val in test_values:
        print(reverse_integer(val))