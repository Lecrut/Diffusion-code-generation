def calculate_year_difference(year1_str: str, year2_str: str) -> int:
    year1 = int(year1_str)
    year2 = int(year2_str)
    return year1 - year2

if __name__ == '__main__':
    difference1 = calculate_year_difference('2020', '1990')
    print(difference1)
    difference2 = calculate_year_difference('2020', '2010')
    print(difference2)
    difference3 = calculate_year_difference('2023', '1990')
    print(difference3)