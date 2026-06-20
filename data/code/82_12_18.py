def find_numerical_gap(year1, year2):
    return abs(year1 - year2)

if __name__ == '__main__':
    start_year = 2023
    end_year = 1985
    gap = find_numerical_gap(start_year, end_year)
    print(gap)