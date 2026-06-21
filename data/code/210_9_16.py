import statistics

def compute_range(data):
    if not isinstance(data, list) or not all((isinstance(x, (int, float)) for x in data)):
        raise ValueError('Input must be a non-empty list of numbers.')
    return max(data) - min(data)
if __name__ == '__main__':
    sample_dataset1 = [10, 5, 20, 15]
    sample_dataset2 = [3.5, 8.2, 1.7, 9.4, 4.0]
    print(compute_range(sample_dataset1))
    print(compute_range(sample_dataset2))