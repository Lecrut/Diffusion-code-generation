def calculate_average(sample):
    return sum(x for x in sample) / len(sample)

if __name__ == '__main__':
    sample = [50, 60, 70]
    print(calculate_average(sample))