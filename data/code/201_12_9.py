MEAN_CONSTANTS = {
    'INVALID_TYPE_MESSAGE': "All elements in the iterable must be floats"
}

def calculate_mean(values):
    if not all(isinstance(x, float) for x in values):
        raise TypeError(MEAN_CONSTANTS['INVALID_TYPE_MESSAGE'])
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    print(calculate_mean(sample_values))