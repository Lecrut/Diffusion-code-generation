def calculate_year_difference(year1, year2):
    difference = year1 - year2
    return abs(difference)

if __name__ == '__main__':
    sample_years_1 = 2030
    sample_years_2 = 1985
    result = calculate_year_difference(sample_years_1, sample_years_2)
    print(f"The difference between {sample_years_1} and {sample_years_2} is: {result}")