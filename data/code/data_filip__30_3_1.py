import sys

def int_to_binary_string(n):
    if n == 0:
        return '0'
    is_negative = n < 0
    if is_negative:
        n = -n
    result = []
    while n > 0:
        result.append('1' if n & 1 else '0')
        n >>= 1
    binary_str = ''.join(reversed(result))
    if is_negative:
        return '-' + binary_str
    return binary_str

if __name__ == '__main__':
    sample_values = [0, 1, 2, 15, 255, 1023, 65535, -1, -42, 1234567890]
    for val in sample_values:
        converted = int_to_binary_string(val)
        print(f"{val} -> {converted}")