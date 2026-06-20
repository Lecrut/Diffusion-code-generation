def calculate_year_difference(year1, year2):
    return abs(year2 - year1)

if __name__ == '__main__':
    test_cases = [
        (2000, 2020),
        (1990, 2010),
        (2020, 2000),
        (2010, 2000),
        (2000, 2000),
        (100, 2000),
        (1000, 500)
    ]
    
    for year1, year2 in test_cases:
        print(f"Year difference between {year1} and {year2}: {calculate_year_difference(year1, year2)}")