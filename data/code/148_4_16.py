def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_data = [42, 7, 36, 85, 19, 23]
    print(f"Largest in {sample_data}: {find_largest(sample_data)}")