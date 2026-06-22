def find_median(samples):
    samples.sort()
    return samples[2]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5]
    print(find_median(sample_values))