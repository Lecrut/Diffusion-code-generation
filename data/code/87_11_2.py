def test_conditions(x, y):
    return x > 5 and y < 10

if __name__ == '__main__':
    conditions = {'x': 6, 'y': 8}
    result = test_conditions(conditions['x'], conditions['y'])
    print(result)