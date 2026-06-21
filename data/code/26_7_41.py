is_greater_than = lambda x, y: x > y

if __name__ == '__main__':
    sample_values_1 = {'x': 25, 'y': 20}
    result_1 = is_greater_than(sample_values_1['x'], sample_values_1['y'])
    print(result_1)

    sample_values_2 = {'x': 4, 'y': 9}
    result_2 = is_greater_than(sample_values_2['x'], sample_values_2['y'])
    print(result_2)