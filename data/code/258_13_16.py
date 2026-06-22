def compute_pair_averages(pair1, pair2):
    return tuple((x + y) / 2 for x, y in zip(pair1, pair2))

if __name__ == '__main__':
    sample_values = {
        'pair1': (7, 14, 21),
        'pair2': (3, 6, 9)
    }
    averages = compute_pair_averages(sample_values['pair1'], sample_values['pair2'])
    print(averages)