def binary_to_hex(binary_string):
    if not binary_string:
        return ""
    if not all(c in '01' for c in binary_string):
        raise ValueError("Input must be a binary string containing only 0s and 1s")
    
    padding = (4 - len(binary_string) % 4) % 4
    padded_binary = '0' * padding + binary_string
    
    chunks = [padded_binary[i:i+4] for i in range(0, len(padded_binary), 4)]
    hex_chars = []
    
    for chunk in chunks:
        value = int(chunk, 2)
        hex_chars.append(format(value, 'x'))
    
    return ''.join(hex_chars)

if __name__ == '__main__':
    sample_input = "110101100111"
    result = binary_to_hex(sample_input)
    print(result)
    
    large_sample = "1" * 10000
    large_result = binary_to_hex(large_sample)
    print(len(large_result))