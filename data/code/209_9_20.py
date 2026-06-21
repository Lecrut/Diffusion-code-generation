def calculate_average(sample):
    total = sum(x for x in sample)
    count = len(sample)
    return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_values = [50, 60, 70]
    avg = calculate_average(sample_values)
    print(avg)