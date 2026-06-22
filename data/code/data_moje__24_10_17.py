def is_leap_year(year: int) -> bool:
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    return (year & 3 == 0) and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':
    results = []
    for test_year in (2000, 1900, 2024, 2023, 400, -100):
        results.append(is_leap_year(test_year))
    for val in results:
        print(val)