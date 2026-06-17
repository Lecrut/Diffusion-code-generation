import re
def parse_input(value: str) -> float | None:
    pattern = r'^([+-]?[0-9]*\.?[0-9]+)[\s]*(L|l|[gG][aA]|gal)$'
    match = re.match(pattern, value.strip())
    if not match:
        raise ValueError("Invalid input format. Expected a number followed by 'L/l', '[gG]al'.")
    try:
        num_str = match.group(1)
        return float(num_str), match.group(2).lower()
    except ValueError as e:
        raise ValueError(f"Cannot convert '{num_str}' to float.") from e
def liters_to_gallons(liters: float) -> str:
    if not isinstance(liters, (int, float)):
        raise TypeError("Input must be a numeric value representing liters.")
    return f"{liters / 3.78541178:.2f} gal"
def gallons_to_liters(gallons: float) -> str:
    if not isinstance(gallons, (int, float)):
        raise TypeError("Input must be a numeric value representing gallons.")
    return f"{gallons * 3.78541178:.2f} L"
def convert_volume(input_str: str) -> tuple[str | None, str]:
    try:
        value, unit = parse_input(input_str)
        if not isinstance(value, (int, float)):
            raise ValueError("Numeric conversion failed.")
        result_unit = "gal" if unit in ("l", "L") else "L"
        if result_unit == "gal":
            converted_value = liters_to_gallons(value)
        else:
            converted_value = gallons_to_liters(value)
        return input_str, converted_value.strip()
    except (ValueError, TypeError):
        raise
if __name__ == '__main__':
    test_cases = [
        "5 L",
        "10 l",
        "[gG]al 2.34",
        "7 gallons",
        "invalid input",
        "abc xyz"
    ]
    for case in test_cases:
        try:
            original, result = convert_volume(case)
            print(f"{original} -> {result}")
        except ValueError as e:
            print(f"Error processing '{case}': {e}")