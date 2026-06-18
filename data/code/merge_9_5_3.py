def calculate_average(numbers):
    if not numbers:
        return 0
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    result = calculate_average(data)
    print(result)