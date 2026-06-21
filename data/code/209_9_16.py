def average_sample(sample):
    if not sample:
        return 0
    total = sum(x for x in sample)
    count = len(sample)
    return total / count

if __name__ == '__main__':
    sample = [50, 60, 70]
    avg = average_sample(sample)
    print(avg)