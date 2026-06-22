def calculate_average(values):
    total = 0
    count = 0
    for value in values:
        total += value
        count += 1
    return total / count

if __name__ == '__main__':
    sample_values = [3, 5, 7, 9, 11]
    average = calculate_average(sample_values)
    print(average)