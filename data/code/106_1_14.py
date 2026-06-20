def calculate_year_difference(year1, year2):
    return abs(year1 - year2)

if __name__ == '__main__':
    sample_years = [(2023, 1998), (2000, 2024), (1850, 1900)]
    for start_year, end_year in sample_years:
        result = calculate_year_difference(start_year, end_year)
        print(f"The difference between {start_year} and {end_year} is {result} year(s).")