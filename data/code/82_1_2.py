def calculate_year_difference(year1, year2):
    if year1 > year2:
        return year1 - year2
    else:
        return year2 - year1
if __name__ == '__main__':
    y1 = 2023
    y2 = 1990
    difference = calculate_year_difference(y1, y2)
    print(difference)