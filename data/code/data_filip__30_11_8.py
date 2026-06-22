def decimal_to_binary_string(n):
    if n == 0:
        return '0'
    result = ''
    num = abs(n)
    while num > 0:
        result = str(num % 2) + result
        num //= 2
    if n < 0:
        result = '-' + result
    return result

if __name__ == '__main__':
    sample_value = 42
    print(decimal_to_binary_string(sample_value))