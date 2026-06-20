def validate_years(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both arguments must be integers.")
    if year1 < 0 or year2 < 0:
        raise ValueError("Years cannot be negative.")

def year_difference(y1, y2):
    validate_years(y1, y2)
    return abs(y1 - y2)

if __name__ == '__main__':
    y_a = 2024
    y_b = 1998
    result = year_difference(y_a, y_b)
    print(result)