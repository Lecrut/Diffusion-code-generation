def bin_to_hex(bin_string):
    bin_string = bin_string.replace(' ', '').replace('\n', '')
    if not all(c in '01' for c in bin_string):
        raise ValueError("Input must contain only binary digits 0 and 1")
    
    hex_digits = '0123456789ABCDEF'
    padding = (4 - len(bin_string) % 4) % 4
    padded_bin = '0' * padding + bin_string
    
    result = []
    for i in range(0, len(padded_bin), 4):
        chunk = padded_bin[i:i+4]
        value = int(chunk, 2)
        result.append(hex_digits[value])
    
    return ''.join(result)

if __name__ == '__main__':
    sample_binary = "1101011001011111"
    print(bin_to_hex(sample_binary))
    sample_binary_short = "101"
    print(bin_to_hex(sample_binary_short))
    sample_binary_mixed = "1010 1100 1111"
    print(bin_to_hex(sample_binary_mixed))