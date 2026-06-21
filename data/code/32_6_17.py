class BinaryToHexConverter:
    @staticmethod
    def convert(binary_sequence: str) -> str:
        if not isinstance(binary_sequence, str):
            raise TypeError("Input must be a string")
        if not all(c in '01' for c in binary_sequence):
            raise ValueError("Input must contain only 0s and 1s")
        if not binary_sequence:
            return "0"
        decimal_value = int(binary_sequence, 2)
        hex_string = format(decimal_value, 'x').upper()
        return hex_string

if __name__ == '__main__':
    converter = BinaryToHexConverter()
    sample_inputs = ["1010", "11110000", "1", "0", "11001100"]
    for binary_seq in sample_inputs:
        result = converter.convert(binary_seq)
        print(result)