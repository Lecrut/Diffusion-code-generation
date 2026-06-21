leap_year = lambda y: (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

if __name__ == '__main__':
    test_years = [2000, 1900, 2004, 2003]
    results = [leap_year(y) for y in test_years]
    print(results)