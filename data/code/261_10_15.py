def find_median(sample):
    sample.sort()
    return sample[2]

if __name__ == '__main__':
    samples = [3, 1, 4, 1, 5]
    print(find_median(samples))