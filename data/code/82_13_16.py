def validate_years(y1, y2):
    if not isinstance(y1, int) or not isinstance(y2, int):
        raise ValueError("Both inputs must be integers")
    if y1 < 0 or y2 < 0:
        raise ValueError("Years must be non-negative")

def year_difference(y1, y2):
    validate_years(y1, y2)
    return abs(y1 - y2)

if __name__ == '__main__':
    y_a = 2024
    y_b = 1998
    result = year_difference(y_a, y_b)
    print(result)