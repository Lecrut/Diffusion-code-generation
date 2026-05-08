def find_largest_manual(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest
if __name__ == '__main__':
    sample_list_1 = [10, 5, 22, 8, 30, 15]
    sample_list_2 = [-5, -1, -10, -3]
    sample_list_3 = [42]
    sample_list_4 = []
    print(f"List: {sample_list_1}, Largest: {find_largest_manual(sample_list_1)}")
    print(f"List: {sample_list_2}, Largest: {find_largest_manual(sample_list_2)}")
    print(f"List: {sample_list_3}, Largest: {find_largest_manual(sample_list_3)}")
    try:
        print(f"List: {sample_list_4}, Largest: {find_largest_manual(sample_list_4)}")
    except ValueError as e:
        print(f"Error for empty list: {e}")