def calculate_year_difference(year1: str, year2: str) -> int:
    YEAR_CONVERSION = 1
    return abs(int(year1) - int(year2)) * YEAR_CONVERSION

if __name__ == '__main__':
    result = calculate_year_difference('2023', '2019')
    print(result)