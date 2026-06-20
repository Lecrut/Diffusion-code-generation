def calculate_year_difference(year1: int, year2: int) -> int:
    return abs(year1 - year2)

if __name__ == '__main__':
    result = calculate_year_difference(2023, 1985)
    print(result)