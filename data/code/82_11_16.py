def calculate_year_difference(year1: int, year2: int) -> int:
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both inputs must be integers")
    return abs(year1 - year2)

if __name__ == '__main__':
    year_a = 2023
    year_b = 1990
    difference = calculate_year_difference(year_a, year_b)
    print(difference)