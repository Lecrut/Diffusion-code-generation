def average_sample(sample):
    if not sample:
        raise ValueError("Sample cannot be empty")
    return sum(x for x in sample) / len(sample)

if __name__ == '__main__':
    sample = [50, 60, 70]
    print(average_sample(sample))