def binary_to_hex(binary_string: str) -> str:
    cleaned_input = binary_string.strip()
    if not cleaned_input:
        raise ValueError("Input string cannot be empty")
    
    valid_chars = set("01")
    if any(char not in valid_chars for char in cleaned_input):
        raise ValueError("Input contains invalid binary characters. Only '0' and '1' are allowed.")
    
    decimal_value = int(cleaned_input, 2)
    hex_value = hex(decimal_value)[2:].upper()
    return hex_value

if __name__ == "__main__":
    sample_values = ["1010", "11110000", "0", "11010101"]
    for value in sample_values:
        print(binary_to_hex(value))