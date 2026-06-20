def calculate_year_difference(year1, year2):
    if not (isinstance(year1, int) and isinstance(year2, int)):
        raise ValueError("Both arguments must be integers.")
    return abs(year1 - year2)

if __name__ == '__main__':
    a = 2024
    b = 1999
    result = calculate_year_difference(a, b)
    print(result)