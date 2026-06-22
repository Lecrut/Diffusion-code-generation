def find_median(samples):
    samples.sort()
    return samples[2]

if __name__ == '__main__':
    print(find_median([3, 1, 4, 1, 5]))