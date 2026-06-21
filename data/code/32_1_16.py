def binary_to_hex(bin_list):
    def int_to_hex(n):
        if n == 0:
            return '0'
        hex_chars = '0123456789ABCDEF'
        result = []
        is_negative = n < 0
        if is_negative:
            n = -n
        while n > 0:
            remainder = n & 0xF
            result.append(hex_chars[remainder])
            n = n >> 4
        if is_negative:
            result.append('-')
        return ''.join(reversed(result))

    return [int_to_hex(num) for num in bin_list]

if __name__ == '__main__':
    print(binary_to_hex([15, 10, 255, 0, 16]))