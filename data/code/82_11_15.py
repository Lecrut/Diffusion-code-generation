def year_difference(year1: int, year2: int) -> int:
    return abs(year1 - year2)

if __name__ == '__main__':
    years = { 'year_a': 2023, 'year_b': 1990 }
    difference = year_difference(years['year_a'], years['year_b'])
    print(difference)