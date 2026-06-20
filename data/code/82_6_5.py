def year_difference(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both inputs must be integers.")
    return year1 - year2

if __name__ == '__main__':
    try:
        print(year_difference(2024, 2020))
        print(year_difference(1990, 2000))
        print(year_difference(2025, 2025))
        print(year_difference(1800, 1750))
    except ValueError as e:
        print(e)