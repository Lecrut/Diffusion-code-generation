def non_negative_difference(a, b):
    return max(0, abs(a - b))

if __name__ == '__main__':
    sample_values = {'first': 25, 'second': 35}
    print(non_negative_difference(sample_values['first'], sample_values['second']))