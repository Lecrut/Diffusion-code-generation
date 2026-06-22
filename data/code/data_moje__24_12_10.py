is_leap = lambda y: (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

if __name__ == '__main__':
    years = [2000, 1900, 2024, 2023, 2400, 1800, 2020, 2019]
    results = {y: is_leap(y) for y in years}
    print(results)