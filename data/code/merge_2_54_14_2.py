def find_middle_index(data):
    if not data:
        raise ValueError("Input list cannot be empty.")
    length = len(data)
    middle_position = (length - 1) // 2
    return {
        "middle_value": data[middle_position],
        "index": middle_position,
        "total_elements": length
    }
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        result = find_middle_index(sample_list)
        print(f"Middle value: {result['middle_value']}")
        print(f"Index: {result['index']}")
        print(f"Total elements: {result['total_elements']}")
        sample_even = [1, 2, 3]
        result_even = find_middle_index(sample_even)
        print(f"\nEven-length test:")
        print(f"Middle value: {result_even['middle_value']}")
    except ValueError as e:
        print(f"Error occurred: {e}")