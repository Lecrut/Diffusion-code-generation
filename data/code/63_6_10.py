def reverse_integer(x: int) -> int:
    if x < 0:
        sign = -1
        digits = []
        temp = -x
    else:
        sign = 1
        digits = []
        temp = x
    
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    
    if not digits:
        return 0
    
    reversed_num = 0
    for digit in digits:
        reversed_num = reversed_num * 10 + digit
    
    result = sign * reversed_num
    min_32 = -(2**31)
    max_32 = 2**31 - 1
    
    if result < min_32 or result > max_32:
        return 0
    
    return result

if __name__ == '__main__':
    sample_values = [123, -123, 1534236469, 0, 10, -2147483648]
    for value in sample_values:
        print(reverse_integer(value))