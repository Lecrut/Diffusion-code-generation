def calculate_year_difference(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both inputs must be integers.")
    return abs(year1 - year2)

if __name__ == '__main__':
    try:
        result = calculate_year_difference(2023, 1985)
        print(result)
    except ValueError as e:
        print(e)