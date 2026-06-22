is_leap = lambda y: y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

if __name__ == '__main__':
    years = [2000, 1900, 2004, 2001]
    results = list(map(is_leap, years))
    for y, r in zip(years, results):
        print(y, r)