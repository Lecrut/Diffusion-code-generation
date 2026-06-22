def reverse_digits(n):
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    
    reversed_n *= sign
    max_int = 2**31 - 1
    min_int = -2**31
    
    if reversed_n < min_int or reversed_n > max_int:
        return 0
    
    return reversed_n

if __name__ == '__main__':
    sample_values = [123, -456, 120, 0, 1534236469]
    for val in sample_values:
        result = reverse_digits(val)
        print(result)