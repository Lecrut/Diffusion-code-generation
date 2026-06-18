import re
def parse_volume(input_str: str) -> float | None:
    pattern = r'(\d+\.?\d*)\s*(L|l|liters?|gallons?)?'
    match = re.match(pattern, input_str.strip(), re.IGNORECASE)
    if not match:
        return None
    try:
        value = float(match.group(1))
        unit = match.group(2).lower() if match.group(2) else 'L'
        if abs(value) > 1e6 or (value < -50 and value > 50):
            raise ValueError("Volume out of acceptable range.")
        return {
            "value": value,
            "unit": unit,
            "is_gallons": unit in ('g', 'gal')
        }
    except (ValueError, OverflowError) as e:
        if isinstance(e, ValueError):
            raise ValueError(f"Invalid numeric format or range.") from None
        else:
            raise
def convert_volume(value: float | int, is_gallons: bool = False) -> str:
    try:
        if isinstance(value, (int, float)):
            val = value
        elif isinstance(value, dict):
            val = value["value"]
            is_gallons = value.get("is_gallons", False)
        conversion_factor = 3.785411784 if not is_gallons else 0.264172052
        result_liters = val * conversion_factor
        return f"{result_liters:.2f} L"
    except Exception as e:
        raise ValueError(f"Conversion failed due to invalid input.") from None
def main():
    test_cases = [
        "5.0",                                                     
        "10 L",                           
        "2 gallons",                          
        "3 g",                                      
        "invalid input",                                            
    ]
    for item in test_cases:
        try:
            parsed = parse_volume(item)
            if not isinstance(parsed, dict):
                print(f"Error parsing '{item}': {parsed}")
                continue
            value = parsed["value"]
            is_gallons = parsed.get("is_gallons", False)
            result_str = convert_volume(value, not is_gallons if item.endswith('L') else True)
            print(f"Input: '{item}' -> Output: {result_str}")
        except ValueError as e:
            print(f"Error processing '{item}': {e}")
if __name__ == '__main__':
    main()