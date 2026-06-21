def find_largest_with_list_comprehension(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = max(data)
    return largest

if __name__ == '__main__':
    sample_list_1 = [3, 5, 2, 8, 4]
    result_1 = find_largest_with_list_comprehension(sample_list_1)
    print(f"List: {sample_list_1}, Largest: {result_1}")

    sample_list_2 = [-7, -3, -9, -1]
    result_2 = find_largest_with_list_comprehension(sample_list_2)
    print(f"List: {sample_list_2}, Largest: {result_2}")