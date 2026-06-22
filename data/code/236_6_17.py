def repeat_polygon(polygon, multiplier):
    return [polygon] * multiplier

if __name__ == '__main__':
    sample_polygon = {'vertices': [(0, 0), (1, 0), (1, 1)], 'color': 'blue'}
    multiplier = 3
    result = repeat_polygon(sample_polygon, multiplier)
    print(result)