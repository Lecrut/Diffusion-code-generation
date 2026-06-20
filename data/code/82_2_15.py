def calculate_year_difference(year1: str, year2: str) -> int:
    YEAR_CONVERSION_FACTOR = 1000000000

    def string_to_int_with_conversion(s):
        return int(s) * YEAR_CONVERSION_FACTOR

    difference = abs(string_to_int_with_conversion(year1) - string_to_int_with_conversion(year2))
    return difference // YEAR_CONVERSION_FACTOR

if __name__ == '__main__':
    print(calculate_year_difference('2023', '1990'))