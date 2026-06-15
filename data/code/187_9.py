def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest
if __name__ == '__main__':
    sample_list_one = [10, 4, 25, 8, 30]
    sample_list_two = [-5, -1, -10, -2]
    sample_list_three = [7]
    sample_list_empty = []
    print(f"List 1: {sample_list_one}")
    print(f"Largest in List 1: {find_largest(sample_list_one)}")
    print("-" * 20)
    print(f"List 2: {sample_list_two}")
    print(f"Largest in List 2: {find_largest(sample_list_two)}")
    print("-" * 20)
    print(f"List 3: {sample_list_three}")
    print(f"Largest in List 3: {find_largest(sample_list_three)}")
    print("-" * 20)
    try:
        find_largest(sample_list_empty)
    except ValueError as e:
        print(f"Error for empty list: {e}")