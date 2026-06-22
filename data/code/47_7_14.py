def mean(numbers):
    if not numbers:
        raise ValueError("Cannot compute mean of empty list")
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result = mean(sample_values)
    print(result)