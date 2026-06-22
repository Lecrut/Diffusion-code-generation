def find_median(samples):
    samples.sort()
    return samples[2]

if __name__ == '__main__':
    sample_values = [10, 5, 8, 12, 3]
    print(find_median(sample_values))