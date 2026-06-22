def reverse_integer(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    reversed_num = 0
    
    while x_abs != 0:
        digit = x_abs % 10
        reversed_num = reversed_num * 10 + digit
        x_abs //= 10
    
    reversed_num *= sign
    
    if reversed_num < INT_MIN or reversed_num > INT_MAX:
        return 0
    
    return reversed_num

if __name__ == '__main__':
    sample_values = [123, -123, 120, 0, 1534236469, -2147483648, 2147483647]
    for val in sample_values:
        result = reverse_integer(val)
        print(result)