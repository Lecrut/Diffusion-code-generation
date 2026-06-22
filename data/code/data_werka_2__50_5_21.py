def non_negative_difference(a, b):
    return (a - b) if a >= b else (b - a)

if __name__ == '__main__':
    sample_values = {'x': 15, 'y': 7}
    print(non_negative_difference(sample_values['x'], sample_values['y']))