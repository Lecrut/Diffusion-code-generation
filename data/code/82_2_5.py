def calculate_year_difference(year1: str, year2: str) -> int:
    try:
        year1_int = int(year1)
        year2_int = int(year2)
        return abs(year1_int - year2_int)
    except ValueError:
        raise ValueError("Input must be strings representing valid integers.")

if __name__ == '__main__':
    difference = calculate_year_difference('2023', '1990')
    print(f"The difference between 2023 and 1990 is: {difference}")