def binary_ints_to_hex_strings(binary_ints):
    hex_strings = []
    for num in binary_ints:
        hex_val = 0
        temp = num
        position = 0
        while temp > 0:
            bit = temp & 1
            if bit:
                hex_val |= (1 << position)
            temp >>= 1
            position += 1
        hex_str = ""
        temp_hex = hex_val
        if temp_hex == 0:
            hex_str = "0"
        else:
            while temp_hex > 0:
                nibble = temp_hex & 0xF
                if nibble < 10:
                    char = chr(nibble + ord('0'))
                else:
                    char = chr(nibble - 10 + ord('A'))
                hex_str = char + hex_str
                temp_hex >>= 4
        hex_strings.append(hex_str)
    return hex_strings

if __name__ == '__main__':
    sample_binary_ints = [0, 1, 10, 255, 123456789]
    result = binary_ints_to_hex_strings(sample_binary_ints)
    print(result)