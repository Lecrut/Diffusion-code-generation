THRESHOLD = 1e-09

def calculate_average(numbers):
    total_sum = 0
    count = 0
    for number in numbers:
        total_sum += number
        count += 1
    if count < THRESHOLD:
        return 0.0
    return total_sum / count
if __name__ == '__main__':
    sample_numbers = [1, 2, 3]
    average = calculate_average(sample_numbers)
    print(average)