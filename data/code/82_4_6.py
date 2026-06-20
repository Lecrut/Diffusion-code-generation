def calculate_year_difference(year1: int, year2: int) -> int:
    return year1 - year2

if __name__ == '__main__':
    year_x = 2030
    year_y = 2000
    difference = calculate_year_difference(year_x, year_y)
    print(difference)