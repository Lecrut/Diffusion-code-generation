def compute_average(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    average = compute_average(sample_numbers)
    print(average)