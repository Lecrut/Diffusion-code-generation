def sum_three(a, b, c):
    return a + b + c

if __name__ == '__main__':
    sample_values = {'x': 10, 'y': 20, 'z': 30}
    result = sum_three(sample_values['x'], sample_values['y'], sample_values['z'])
    print(result)