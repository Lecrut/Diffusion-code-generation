def compute_average(values):
    total = sum(values)
    count = len(values)
    average = total / count if count > 0 else float('nan')
    return average

if __name__ == '__main__':
    sample_data = [3.5, 2.1, 4.8, 6.7]
    avg = compute_average(sample_data)
    print(avg)