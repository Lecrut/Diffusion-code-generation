def calculate_average(numbers):
    if not numbers:
        raise ValueError("The sequence is empty")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numbers")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_sequence = [10.5, 20.3, 30.7]
    try:
        average = calculate_average(sample_sequence)
        print(f"The average is: {average}")
    except (ValueError, TypeError) as e:
        print(e)