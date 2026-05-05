def calculate_difference(year1, year2):
    return abs(year1 - year2)
if __name__ == '__main__':
    years = [2023, 2025, 2021, 2024]
    for year_a in years:
        for year_b in years:
            if year_a != year_b:
                difference = calculate_difference(year_a, year_b)
                print(f"Difference between {year_a} and {year_b} is {difference}")