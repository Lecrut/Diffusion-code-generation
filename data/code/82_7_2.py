def calculate_difference(year1, year2):
    return abs(year1 - year2)
if __name__ == '__main__':
    years_to_check = [2023, 2025, 2021, 2024]
    for year1 in years_to_check:
        for year2 in years_to_check:
            difference = calculate_difference(year1, year2)
            print(f"Difference between {year1} and {year2} is {difference}")