def find_max_in_tuple(numbers):
    if not numbers:
        return None
    try:
        return max(numbers)
    except TypeError:
        return "Error: Invalid input detected"

if __name__ == '__main__':
    sample_numbers = (3, 5, 1, 8, 2)
    max_val = find_max_in_tuple(sample_numbers)
    print(max_val)