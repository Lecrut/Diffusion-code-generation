def year_difference(y1, y2):
    return abs(y1 - y2)

if __name__ == '__main__':
    years = {'y_a': 2024, 'y_b': 1998}
    result = year_difference(years['y_a'], years['y_b'])
    print(result)