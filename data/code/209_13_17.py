def calculate_average(values):
    total = sum(values)
    count = len(values)
    if count == 0:
        return 0
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [20, 40, 60, 80, 100]
    result = calculate_average(sample_values)
    print(result)