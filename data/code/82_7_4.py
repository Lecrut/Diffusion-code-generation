def calculate_difference(year1, year2):
    return abs(year1 - year2)
if __name__ == '__main__':
    years_to_test = [
        (2024, 2026),
        (1990, 1992),
        (2050, 2052),
        (2000, 2001)
    ]
    for year1, year2 in years_to_test:
        difference = calculate_difference(year1, year2)
        print(f"Year 1: {year1}, Year 2: {year2}, Difference: {difference}")