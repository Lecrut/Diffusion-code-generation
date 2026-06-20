def year_difference(year1: int, year2: int) -> int:
    return abs(year1 - year2)

if __name__ == '__main__':
    print(year_difference(2023, 1990))
    print(year_difference(2000, 2024))
    print(year_difference(1850, 1850))