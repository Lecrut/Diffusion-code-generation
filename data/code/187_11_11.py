def find_largest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    largest = max(numbers)
    return largest

if __name__ == '__main__':
    sample_values = {
        "list1": [3, 1, 4, 1, 5, 9, 2],
        "list2": [-10, -5, -20, -1],
        "list3": [7],
        "list4": []
    }

    for key, value in sample_values.items():
        try:
            print(f"The largest number in {key} is: {find_largest(value)}")
        except ValueError as e:
            print(e)