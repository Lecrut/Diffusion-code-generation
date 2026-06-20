def validate_year(year_str: str) -> int:
    try:
        year = int(year_str)
        if year < 0:
            raise ValueError("Year cannot be negative")
        return year
    except ValueError as e:
        raise ValueError(f"Invalid year format: {year_str}") from e

def calculate_year_difference(year1: str, year2: str) -> int:
    year1_int = validate_year(year1)
    year2_int = validate_year(year2)
    return abs(year1_int - year2_int)

if __name__ == '__main__':
    result = calculate_year_difference('2023', '1990')
    print(f"The difference between 2023 and 1990 is: {result}")