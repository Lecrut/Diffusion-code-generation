def calculate_year_difference(year1, year2):
    return abs(year1 - year2)
if __name__ == '__main__':
    print(calculate_year_difference(2023, 1998))
    print(calculate_year_difference(2000, 2024))
    print(calculate_year_difference(1900, 1900))