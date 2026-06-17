import re
def parse_volume(value: str) -> float:
    pattern = r'^(\d+\.?\d*)\s*(L|l|liters?|gal|gallons?)$'
    match = re.match(pattern, value.strip())
    if not match:
        raise ValueError(f"Invalid input format. Expected 'number L/l/Liters/Gallons/gal'. Got '{value}'")
    return float(match.group(1))
def convert_volume(liters: float) -> float:
    conversion_factor = 0.264172052
    return round(liters * conversion_factor, 2)
if __name__ == '__main__':
    test_cases = [
        "3.5 L",
        "10 Liters",
        "2 gal",
        "5 gallons"
    ]
    for case in test_cases:
        try:
            liters = parse_volume(case)
            gallons = convert_volume(liters)
            print(f"{case} -> {gallons:.2f}")
        except ValueError as e:
            print(e)