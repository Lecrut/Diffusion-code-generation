def calculate_pair_averages(pair1, pair2):
    return tuple((x + y) / 2 for x, y in zip(pair1, pair2))

if __name__ == '__main__':
    sample_values = {
        'pair1': (10, 20, 30),
        'pair2': (40, 50, 60)
    }
    result = calculate_pair_averages(sample_values['pair1'], sample_values['pair2'])
    print(result)