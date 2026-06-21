def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list = [3, 7, -2, 8, 5]
    print(f"The largest number in {sample_list} is: {find_largest(sample_list)}")