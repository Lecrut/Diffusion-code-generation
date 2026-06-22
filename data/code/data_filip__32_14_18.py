def binary_to_hex(binary_string):
    if not binary_string:
        return ''
    num_value = int(binary_string, 2)
    return format(num_value, 'x')

if __name__ == '__main__':
    sample_binary = '10101011'
    result = binary_to_hex(sample_binary)
    print(result)

    sample_binary_large = '1' * 1000
    result_large = binary_to_hex(sample_binary_large)
    print(result_large)

    sample_empty = ''
    result_empty = binary_to_hex(sample_empty)
    print(repr(result_empty))