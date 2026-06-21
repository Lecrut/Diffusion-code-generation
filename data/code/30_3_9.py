def int_to_binary_string(n):
    if n == 0:
        return '0'
    result = []
    while n > 0:
        result.append('1' if n & 1 else '0')
        n >>= 1
    return ''.join(reversed(result))

def int_to_binary_string_with_sign(n):
    if n < 0:
        return '-' + int_to_binary_string(-n)
    return int_to_binary_string(n)

if __name__ == '__main__':
    test_values = [0, 1, 2, 5, 10, 255, 1024, 123456789012345678901234567890]
    for val in test_values:
        binary_result = int_to_binary_string_with_sign(val)
        print(binary_result)