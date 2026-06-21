def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_lists = [
        [3, 1, 4, 1, 5, 9, 2],
        [-10, -5, -20, -1],
        [7],
        []
    ]
    for list in sample_lists:
        try:
            print(f"Largest in {list}: {find_largest(list)}")
        except ValueError as e:
            print(e)