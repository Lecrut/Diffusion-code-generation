def average(numbers):
    if not numbers:
        raise ValueError("The sequence is empty")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numbers")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    print(average(sample_sequence))