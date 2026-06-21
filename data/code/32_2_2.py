def binary_to_hex(binary_str):
    if not binary_str:
        return "0"
    value = 0
    for char in binary_str:
        value = (value << 1) | (1 if char == '1' else 0)
    return hex(value)[2:].upper()

if __name__ == '__main__':
    sample_inputs = ["0", "1", "1010", "11111111", "100000000"]
    for s in sample_inputs:
        print(binary_to_hex(s))