def calculate_year_difference(end_year: int, start_year: int) -> int:
    return abs(end_year - start_year)
if __name__ == '__main__':
    year1 = 2023
    year2 = 1990
    difference = calculate_year_difference(year1, year2)
    print(f"The difference between {year1} and {year2} is: {difference}")