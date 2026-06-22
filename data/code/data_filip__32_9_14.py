def binary_to_hexadecimal(binary_str: str) -> str:
    return hex(int(binary_str, 2))[2:].upper()

if __name__ == '__main__':
    sample_inputs = ['1010', '11110000', '11011011', '0', '1']
    for sample in sample_inputs:
        print(binary_to_hexadecimal(sample))