def find_highest_value(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    return max(numbers)

if __name__ == '__main__':
    sample_values = [4, 2, 9, 6, 3]
    try:
        highest_value = find_highest_value(sample_values)
        print(highest_value)
    except ValueError as e:
        print(e)