def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    result = sign * reversed_num
    if result < -2**31 or result > 2**31 - 1:
        return 0
    return result

if __name__ == '__main__':
    sample_inputs = [123, -456, 120, 0, 1534236469]
    for value in sample_inputs:
        print(reverse_integer(value))