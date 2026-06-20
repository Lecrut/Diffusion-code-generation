def absolute_year_difference(year1: int, year2: int) -> int:
    return abs(year1 - year2)

if __name__ == '__main__':
    years = {'start': 2060, 'end': 1980}
    print(absolute_year_difference(years['start'], years['end']))