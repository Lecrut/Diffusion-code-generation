def calculate_year_difference(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both inputs must be integers.")
    return abs(year1 - year2)

if __name__ == '__main__':
    start_year = 1985
    end_year = 2023
    try:
        result = calculate_year_difference(start_year, end_year)
        print(result)
    except ValueError as e:
        print(e)