def get_twos_complement(n):
    if n == 0:
        return "0"
    is_negative = n < 0
    if is_negative:
        n = -n
    bit_length = n.bit_length()
    binary_str = bin(n)[2:]
    inverted = ''.join('1' if c == '0' else '0' for c in binary_str)
    inverted_num = int(inverted, 2)
    two_complement_num = inverted_num + 1
    result_bin = bin(two_complement_num)[2:]
    if is_negative:
        if len(result_bin) == bit_length:
            result_bin = '1' + result_bin
        else:
            result_bin = '1' + result_bin
        return result_bin
    return binary_str

if __name__ == '__main__':
    test_values = [5, -5, 10, -10, 0, -1]
    for value in test_values:
        print(get_twos_complement(value))