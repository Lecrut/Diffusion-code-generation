def calculate_year_difference(year1: int, year2: int) -> int:
    return abs(year1 - year2)

if __name__ == '__main__':
    test_cases = [
        (2020, 1990),
        (2023, 2010),
        (1985, 2023)
    ]
    
    for year_a, year_b in test_cases:
        difference = calculate_year_difference(year_a, year_b)
        print(f"Year difference between {year_a} and {year_b}: {difference}")