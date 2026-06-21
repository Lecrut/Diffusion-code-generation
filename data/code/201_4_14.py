def average(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return sum(num for num in numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(average(sample_numbers))