def binary_list_to_hex(bins):
    result = []
    for num in bins:
        if num == 0:
            result.append("0")
            continue
        
        is_negative = num < 0
        if is_negative:
            num = num & 0xFFFFFFFF
        
        hex_chars = []
        temp = num
        while temp > 0:
            remainder = temp & 0xF
            if remainder < 10:
                hex_chars.append(chr(ord('0') + remainder))
            else:
                hex_chars.append(chr(ord('A') + remainder - 10))
            temp = temp >> 4
        
        hex_str = "".join(reversed(hex_chars))
        result.append(hex_str)
    return result

if __name__ == '__main__':
    sample_values = [255, 16, 0, -1, 4096, 1024]
    hex_results = binary_list_to_hex(sample_values)
    print(hex_results)