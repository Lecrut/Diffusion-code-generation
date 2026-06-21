def find_min_value(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return min(numbers)

if __name__ == '__main__':
    sample_data = [15, 3, 8, 22, 1]
    try:
        smallest = find_min_value(sample_data)
        print(smallest)
    except ValueError as e:
        print(e)