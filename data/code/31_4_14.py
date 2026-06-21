import sys

def hex_strings_to_ints(hex_strings: list) -> list[int]:
    if not isinstance(hex_strings, list):
        raise TypeError("Input must be a list")
    result = []
    for item in hex_strings:
        if not isinstance(item, str):
            raise TypeError(f"Expected string, got {type(item).__name__}")
        result.append(int(item, 16))
    return result

if __name__ == '__main__':
    sample_data = ["0xFF", "0x10", "AB", "deadbeef"]
    converted_values = hex_strings_to_ints(sample_data)
    print(converted_values)