class BinaryConverter:
    @staticmethod
    def to_hex(binary_sequence: str) -> str:
        if not binary_sequence:
            return "0"
        if not all(c in '01' for c in binary_sequence):
            raise ValueError("Input must contain only 0 and 1")
        decimal_value = int(binary_sequence, 2)
        hex_string = format(decimal_value, 'x')
        return hex_string

if __name__ == '__main__':
    converter = BinaryConverter()
    sample_inputs = ["1010", "11111111", "100000000", "0"]
    for sample in sample_inputs:
        result = converter.to_hex(sample)
        print(f"Binary: {sample} -> Hex: {result}")