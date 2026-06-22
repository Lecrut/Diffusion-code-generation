def mean_of_integers(numbers):
    if not numbers:
        return 0
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = mean_of_integers(sample_values)
    print(result)