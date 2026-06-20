def calculate_average(values):
    total = sum(values)
    count = len(values)
    if count == 0:
        return 0
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [15, 25, 35, 45, 55]
    avg = calculate_average(sample_values)
    print(avg)