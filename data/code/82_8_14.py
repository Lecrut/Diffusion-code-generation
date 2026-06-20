def calculate_year_difference(y1, y2):
    return abs(y1 - y2)

if __name__ == '__main__':
    year_1 = 2023
    year_2 = 1987
    difference = calculate_year_difference(year_1, year_2)
    print(difference)