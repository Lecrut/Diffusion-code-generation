class BinaryConverter:
    @staticmethod
    def to_hex(binary_sequence: str) -> str:
        if not binary_sequence:
            return ""
        if not all(c in '01' for c in binary_sequence):
            raise ValueError("Input must contain only binary digits (0 and 1)")
        padded_length = (len(binary_sequence) + 3) // 4 * 4
        padded_binary = binary_sequence.zfill(padded_length)
        integer_value = int(padded_binary, 2)
        return hex(integer_value)[2:].upper()

if __name__ == '__main__':
    sample_values = ["0101", "11110000", "1", "10101010", ""]
    converter = BinaryConverter()
    for value in sample_values:
        print(converter.to_hex(value))