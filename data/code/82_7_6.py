def calculate_difference(year1, year2):
    return abs(year1 - year2)
if __name__ == '__main__':
    years = [2023, 2025, 2021, 2024]
    for y1 in years:
        for y2 in years:
            if y1 != y2:
                difference = calculate_difference(y1, y2)
                print(f"Difference between {y1} and {y2}: {difference}")