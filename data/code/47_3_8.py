def average_of_integers(numbers):
    if not numbers:
        return 0
    total = sum(number for number in numbers)
    return total / len(numbers)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = average_of_integers(sample_data)
    print(result)