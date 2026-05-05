def calculate_year_difference(year1, year2):
    if year1 > year2:
        return year1 - year2
    else:
        return year2 - year1
if __name__ == '__main__':
    a = 2024
    b = 1990
    result = calculate_year_difference(a, b)
    print(result)