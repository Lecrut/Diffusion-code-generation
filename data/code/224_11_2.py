def compute_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [100, 200, 300]
    avg = compute_average(sample_values)
    print(avg)