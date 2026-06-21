def find_maximum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    max_number = numbers[0]
    for number in numbers[1:]:
        if number > max_number:
            max_number = number
    return max_number

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    try:
        print(f"The maximum of {sample_list} is: {find_maximum(sample_list)}")
    except ValueError as e:
        print(e)