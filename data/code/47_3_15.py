def average_of_integers(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = average_of_integers(sample_values)
    print(result)