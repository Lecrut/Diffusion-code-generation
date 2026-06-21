def validate_sample(sample):
    if not isinstance(sample, list) or not all(isinstance(x, (int, float)) for x in sample):
        raise ValueError("Sample must be a list of numbers")

def average_sample(sample):
    validate_sample(sample)
    return sum(x for x in sample) / len(sample)

if __name__ == '__main__':
    sample = [50, 60, 70]
    print(average_sample(sample))