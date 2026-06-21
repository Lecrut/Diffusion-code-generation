def find_largest_element(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    print(f"Largest in {sample_list}: {find_largest_element(sample_list)}")