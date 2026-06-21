def binary_to_hex(binary_input: str) -> str:
    return hex(int(binary_input, 2))[2:].upper()

if __name__ == '__main__':
    sample_binaries = ['1010', '11110000', '101010101010', '1', '0']
    for binary in sample_binaries:
        print(binary_to_hex(binary))