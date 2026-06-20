def validate_year(year_str: str) -> int:
    if not year_str.isdigit():
        raise ValueError("Invalid year format")
    return int(year_str)

def calculate_year_difference(year1: str, year2: str) -> int:
    year1_int = validate_year(year1)
    year2_int = validate_year(year2)
    return abs(year1_int - year2_int)

if __name__ == '__main__':
    result = calculate_year_difference('2023', '1990')
    print(f"The difference between 2023 and 1990 is: {result}")