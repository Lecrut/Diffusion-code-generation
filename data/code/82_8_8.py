def calculate_year_difference(y1, y2):
    return abs(y1 - y2)

if __name__ == '__main__':
    year_a = 2023
    year_b = 1998
    difference = calculate_year_difference(year_a, year_b)
    print(difference)