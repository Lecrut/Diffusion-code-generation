def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count if count > 0 else None

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(average(sample_numbers))