class BinaryHexManager:
    @staticmethod
    def convert_binary_to_hex(binary_input: str) -> str:
        if not binary_input:
            return "0x0"
        clean_binary = binary_input.strip()
        if clean_binary.startswith("0b") or clean_binary.startswith("0B"):
            clean_binary = clean_binary[2:]
        if not all(c in "01" for c in clean_binary):
            raise ValueError("Invalid binary string")
        decimal_value = int(clean_binary, 2)
        return hex(decimal_value)

if __name__ == '__main__':
    manager = BinaryHexManager()
    test_cases = ["1010", "11111111", "0b1001", "0"]
    for case in test_cases:
        result = manager.convert_binary_to_hex(case)
        print(f"Binary: {case} -> Hex: {result}")
    specific_case = "11011011"
    output = BinaryHexManager.convert_binary_to_hex(specific_case)
    print(f"Converted: {output}")