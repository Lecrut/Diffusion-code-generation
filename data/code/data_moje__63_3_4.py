def reverse_integer(n):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    
    reversed_num = 0
    while n > 0:
        digit = n % 10
        if reversed_num > (INT_MAX - digit) // 10:
            return 0
        reversed_num = reversed_num * 10 + digit
        n //= 10
    
    result = sign * reversed_num
    if result < INT_MIN or result > INT_MAX:
        return 0
    return result

if __name__ == '__main__':
    sample_values = [123, -123, 1534236469, 0, -2147483412]
    for val in sample_values:
        print(reverse_integer(val))