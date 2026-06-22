def average_pairs(tuple1, tuple2):
    return tuple((a + b) / 2 for a, b in zip(tuple1, tuple2))

if __name__ == '__main__':
    sample_values = {
        'pair1': (10, 20, 30),
        'pair2': (40, 50, 60)
    }
    result = average_pairs(sample_values['pair1'], sample_values['pair2'])
    print(result)