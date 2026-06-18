def find_average(numbers):
    if not numbers:
        return 0
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average
if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    result = find_average(sample_sequence)
    print(result)