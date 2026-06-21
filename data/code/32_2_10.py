def binary_to_hex(binary_string):
    if not binary_string:
        return "0"
    if not all(c in '01' for c in binary_string):
        raise ValueError("Input must contain only 0s and 1s")
    decimal_value = int(binary_string, 2)
    return hex(decimal_value)[2:].upper()

if __name__ == '__main__':
    sample_inputs = ["1010", "11110000", "0", "1010101010101010"]
    for s in sample_inputs:
        result = binary_to_hex(s)
        print(f"{s} -> {result}")