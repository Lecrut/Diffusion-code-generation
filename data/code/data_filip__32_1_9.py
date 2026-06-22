def binary_ints_to_hex_strings(binary_ints):
    result = []
    for num in binary_ints:
        if not isinstance(num, int) or num < 0:
            raise ValueError("All items must be non-negative integers")
        hex_str = ""
        if num == 0:
            hex_str = "0"
        else:
            temp = num
            while temp > 0:
                nibble = temp & 0xF
                if nibble < 10:
                    hex_str = chr(ord('0') + nibble) + hex_str
                else:
                    hex_str = chr(ord('A') + (nibble - 10)) + hex_str
                temp = temp >> 4
        result.append(hex_str)
    return result

if __name__ == '__main__':
    sample_binary_ints = [0, 15, 16, 255, 1024, 42]
    hex_strings = binary_ints_to_hex_strings(sample_binary_ints)
    print(hex_strings)