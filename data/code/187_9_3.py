def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest
if __name__ == '__main__':
    sample_list_1 = [10, 4, 25, 8, 30]
    sample_list_2 = [-5, -1, -10, -2]
    sample_list_3 = [7]
    sample_list_4 = []
    print(f"List 1: {sample_list_1}")
    try:
        result_1 = find_largest(sample_list_1)
        print(f"Largest element in List 1: {result_1}")
    except ValueError as e:
        print(f"Error processing List 1: {e}")
    print("-" * 20)
    print(f"List 2: {sample_list_2}")
    try:
        result_2 = find_largest(sample_list_2)
        print(f"Largest element in List 2: {result_2}")
    except ValueError as e:
        print(f"Error processing List 2: {e}")
    print("-" * 20)
    print(f"List 3: {sample_list_3}")
    try:
        result_3 = find_largest(sample_list_3)
        print(f"Largest element in List 3: {result_3}")
    except ValueError as e:
        print(f"Error processing List 3: {e}")
    print("-" * 20)
    print(f"List 4: {sample_list_4}")
    try:
        result_4 = find_largest(sample_list_4)
        print(f"Largest element in List 4: {result_4}")
    except ValueError as e:
        print(f"Error processing List 4: {e}")