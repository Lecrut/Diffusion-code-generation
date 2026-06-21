def find_max_value(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    return max(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    try:
        largest_value = find_max_value(sample_values)
        print(largest_value)
    except ValueError as e:
        print(e)