HEX_MAP = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
}

VALID_BINARY_CHARS = frozenset({"0", "1"})

class BinaryToHexConverter:
    @staticmethod
    def sanitize_input(binary_sequence: str) -> str:
        cleaned = binary_sequence.strip()
        if not cleaned:
            return ""
        for char in cleaned:
            if char not in VALID_BINARY_CHARS:
                raise ValueError("Input contains non-binary characters")
        return cleaned

    @staticmethod
    def pad_binary_sequence(binary_str: str) -> str:
        remainder = len(binary_str) % 4
        if remainder != 0:
            padding_needed = 4 - remainder
            return "0" * padding_needed + binary_str
        return binary_str

    @staticmethod
    def convert_chunks(chunks: list[str]) -> str:
        hex_digits = []
        for chunk in chunks:
            if chunk not in HEX_MAP:
                raise ValueError(f"Invalid binary chunk: {chunk}")
            hex_digits.append(HEX_MAP[chunk])
        return "".join(hex_digits)

    @staticmethod
    def to_hexadecimal(binary_sequence: str) -> str:
        if not isinstance(binary_sequence, str):
            raise TypeError("Input must be a string")

        cleaned = BinaryToHexConverter.sanitize_input(binary_sequence)
        if not cleaned:
            return "0"

        padded = BinaryToHexConverter.pad_binary_sequence(cleaned)
        chunk_size = 4
        chunks = [padded[i:i + chunk_size] for i in range(0, len(padded), chunk_size)]

        return BinaryToHexConverter.convert_chunks(chunks)

if __name__ == '__main__':
    converter_instance = BinaryToHexConverter()
    test_value_1 = "11110000"
    test_value_2 = "10101010"
    test_value_3 = "1"
    test_value_4 = "0000"

    result_1 = converter_instance.to_hexadecimal(test_value_1)
    print(result_1)

    result_2 = converter_instance.to_hexadecimal(test_value_2)
    print(result_2)

    result_3 = converter_instance.to_hexadecimal(test_value_3)
    print(result_3)

    result_4 = converter_instance.to_hexadecimal(test_value_4)
    print(result_4)