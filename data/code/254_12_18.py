def find_min_element(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    minimum = numbers[0]
    for item in numbers[1:]:
        if item < minimum:
            minimum = item
    return minimum

if __name__ == '__main__':
    sample_numbers = [34, 78, 12, 56, 90]
    print(f"Minimum of {sample_numbers}: {find_min_element(sample_numbers)}")