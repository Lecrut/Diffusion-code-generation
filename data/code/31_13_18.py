from typing import Final

def hex_to_decimal(hex_string: str) -> int:
    if not isinstance(hex_string, str):
        raise TypeError("Input must be a string")
    hex_string = hex_string.strip().lower()
    if hex_string.startswith("0x"):
        hex_string = hex_string[2:]
    if not hex_string:
        raise ValueError("Empty input")
    decimal_value: int = 0
    power: int = 1
    for char in reversed(hex_string):
        if "0" <= char <= "9":
            digit_value: int = ord(char) - ord("0")
        elif "a" <= char <= "f":
            digit_value = ord(char) - ord("a") + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        decimal_value += digit_value * power
        power *= 16
    return decimal_value

if __name__ == "__main__":
    sample_hex: Final[str] = "1A3F"
    result: int = hex_to_decimal(sample_hex)
    print(result)