def find_max_index(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    max_value = max(numbers)
    for index, value in enumerate(numbers):
        if value == max_value:
            return index

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    print(find_max_index(sample_values))