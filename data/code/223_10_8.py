def find_max_value(numbers):
    if not numbers:
        raise ValueError("List is empty")
    return max(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2]
    try:
        print(find_max_value(sample_numbers))
    except ValueError as e:
        print(e)