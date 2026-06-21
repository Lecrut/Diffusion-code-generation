def find_smallest_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    smallest = sorted_data[0]
    return smallest

if __name__ == '__main__':
    sample_list = [-9.8, 3.14, -1.5, 2.718, 0.001, 5.0]
    try:
        result = find_smallest_element(sample_list)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")