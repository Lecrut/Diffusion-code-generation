def binary_to_hex(binary_list):
    result = []
    for binary in binary_list:
        decimal_value = 0
        bit_index = 0
        temp = binary
        while temp > 0:
            if temp & 1:
                decimal_value |= (1 << bit_index)
            temp >>= 1
            bit_index += 1
        if decimal_value == 0:
            result.append('0')
        else:
            hex_chars = []
            current = decimal_value
            while current > 0:
                nibble = current & 15
                if nibble < 10:
                    hex_chars.append(chr(ord('0') + nibble))
                else:
                    hex_chars.append(chr(ord('A') + (nibble - 10)))
                current >>= 4
            result.append(''.join(reversed(hex_chars)))
    return result

if __name__ == '__main__':
    print(binary_to_hex([0, 1, 15, 16, 255, 1024]))