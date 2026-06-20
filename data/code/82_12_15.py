def calculate_year_gap(year1, year2):
    gap = abs(year1 - year2)
    return gap

if __name__ == '__main__':
    initial_year = 2023
    final_year = 1985
    computed_gap = calculate_year_gap(initial_year, final_year)
    print(computed_gap)