def find_max(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return max([x for x in numbers])
if __name__ == '__main__':
    sample_data = [3, 7, -2, 9, 1]
    try:
        result = find_max(sample_data)
        print(f"Maximum value is {result}")
    except ValueError as e:
        print(e)