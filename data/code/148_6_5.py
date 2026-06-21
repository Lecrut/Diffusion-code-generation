def find_largest(data):
    if not data:
        raise ValueError("Cannot find the largest element in an empty list.")
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    sample_sequence = [7, 2, 9, 3, 5]
    try:
        result = find_largest(sample_sequence)
        print(f"The largest element in {sample_sequence} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")