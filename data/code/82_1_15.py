def calculate_year_difference(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both inputs must be integers.")
    if year1 < 0 or year2 < 0:
        raise ValueError("Years cannot be negative.")
    return abs(year1 - year2)

if __name__ == '__main__':
    y1 = 2024
    y2 = 1999
    difference = calculate_year_difference(y1, y2)
    print(difference)