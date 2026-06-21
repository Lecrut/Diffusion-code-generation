def find_smallest_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    return sorted_data[0]

if __name__ == '__main__':
    sample_list = [3.14, -1.5, 2.718, -10.0, 0.5, 42.0]
    try:
        result = find_smallest_element(sample_list)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")