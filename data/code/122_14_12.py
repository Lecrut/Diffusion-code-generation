def calculate_average(data):
    total = 0
    count = 0
    for number in data:
        total += number
        count += 1
    return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    average = calculate_average(sample_data)
    print(average)