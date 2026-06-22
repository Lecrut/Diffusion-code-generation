if __name__ == '__main__':
    conditions = {'x': lambda x: x > 10, 'y': lambda y: y < 50}
    x, y = 25, 49
    result = all(conditions[key](value) for key, value in zip(['x', 'y'], [x, y]))
    print(result)