def binary_to_hex(binary_string: str) -> str:
    cleaned_binary = binary_string.replace("0b", "").replace(" ", "")
    if not cleaned_binary:
        return "0"
    if any(char not in "01" for char in cleaned_binary):
        raise ValueError("Input contains invalid binary digits")
    decimal_value = int(cleaned_binary, 2)
    hex_string = hex(decimal_value)[2:].upper()
    if decimal_value == 0:
        return "0"
    return hex_string

if __name__ == "__main__":
    sample_inputs = ["1010", "0b1111", "10000000", "0000"]
    for sample in sample_inputs:
        result = binary_to_hex(sample)
        print(f"{sample} -> {result}")