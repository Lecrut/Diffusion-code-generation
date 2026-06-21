def find_min_value(numbers):
    if not numbers:
        raise ValueError("List is empty")
    return min(numbers)

if __name__ == '__main__':
    sample_data = [42, 15, 89, 3, 77, 21]
    try:
        print(find_min_value(sample_data))
    except ValueError as e:
        print(e)