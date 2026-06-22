def binary_to_hex(binary_string):
    if len(binary_string) % 4 != 0:
        padding = 4 - (len(binary_string) % 4)
        binary_string = '0' * padding + binary_string
    nibbles = [binary_string[i:i+4] for i in range(0, len(binary_string), 4)]
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    hex_map = {n: hex_digits[int(n, 2)] for n in nibbles}
    hex_pairs = [[nib, hex_map[nib]] for nib in nibbles]
    result = ''.join([pair[1] for pair in hex_pairs])
    return result

if __name__ == '__main__':
    sample_binary = "110101111001"
    sample_binary_padded = "1010"
    print(binary_to_hex(sample_binary))
    print(binary_to_hex(sample_binary_padded))