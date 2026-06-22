is_leap = lambda y: (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

if __name__ == '__main__':
    test_years = [2000, 1900, 2024, 2023, 1600, 1700, 1800, 2100, 2004, 1999]
    results = [is_leap(y) for y in test_years]
    for y, r in zip(test_years, results):
        print(f"{y}: {r}")