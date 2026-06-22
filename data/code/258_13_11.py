AVERAGE_FACTOR = 2

def calculate_averages(pair1, pair2):
    return tuple((x + y) / AVERAGE_FACTOR for x, y in zip(pair1, pair2))

if __name__ == '__main__':
    sample_values = {
        'pair1': (10, 20, 30),
        'pair2': (40, 50, 60)
    }
    result = calculate_averages(sample_values['pair1'], sample_values['pair2'])
    print(result)