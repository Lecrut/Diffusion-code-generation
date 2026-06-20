def calculate_sum(values):
    return sum(filter(lambda x: isinstance(x, int), values))

if __name__ == '__main__':
    sample_values = [
        10,
        25,
        'hello',
        30,
        -5
    ]
    print(calculate_sum(sample_values))