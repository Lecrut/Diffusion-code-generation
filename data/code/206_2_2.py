def find_min_value(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    return min(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, -2.1, 0.0]
    try:
        print(find_min_value(sample_values))
    except ValueError as e:
        print(e)