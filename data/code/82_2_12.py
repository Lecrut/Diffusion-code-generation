def calculate_year_difference(year1: str, year2: str) -> int:
    return abs(int(year1) - int(year2))

if __name__ == '__main__':
    year_a = 2023
    year_b = 1985
    difference = calculate_year_difference(str(year_a), str(year_b))
    print(f"The difference between {year_a} and {year_b} is: {difference}")