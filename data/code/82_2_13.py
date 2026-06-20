def calculate_year_difference(year1: str, year2: str) -> int:
    return abs(int(year1) - int(year2))

if __name__ == '__main__':
    result = calculate_year_difference('2023', '1990')
    print(f"The difference between 2023 and 1990 is: {result}")