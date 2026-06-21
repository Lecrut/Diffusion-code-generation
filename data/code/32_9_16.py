def binary_to_hex(binary_string: str) -> str:
    binary_string = binary_string.replace(" ", "").replace("0b", "").replace("0B", "")
    if not binary_string:
        return "0"
    decimal_value = int(binary_string, 2)
    return hex(decimal_value)[2:].upper()

if __name__ == "__main__":
    sample_inputs = ["1010", "11111111", "100000000", "0", "101010101010"]
    for value in sample_inputs:
        result = binary_to_hex(value)
        print(f"Binary: {value} -> Hex: {result}")