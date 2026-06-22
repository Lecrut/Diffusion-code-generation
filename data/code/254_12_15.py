def find_min_element(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_numbers = [15, 23, -4, 0, 9]
    print(f"Minimum of {sample_numbers}: {find_min_element(sample_numbers)}")