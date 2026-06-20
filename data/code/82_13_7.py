def year_difference(y1, y2):
    return abs(y1 - y2)

if __name__ == '__main__':
    years = {'year_a': 2024, 'year_b': 1998}
    result = year_difference(years['year_a'], years['year_b'])
    print(result)