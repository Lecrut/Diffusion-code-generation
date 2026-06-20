def year_gap(year1, year2):
    if not isinstance(year1, int) or not isinstance(year2, int):
        raise ValueError("Both arguments must be integers.")
    if year1 < 0 or year2 < 0:
        raise ValueError("Years cannot be negative.")
    return abs(year1 - year2)

if __name__ == '__main__':
    print(year_gap(2023, 1985))