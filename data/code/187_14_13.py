def find_largest_element(data):
    if not data:
        raise ValueError("Cannot find largest element in an empty list.")
    return max(data)

if __name__ == '__main__':
    sample_list_one = [10, 5, 20, 8]
    try:
        largest_value_one = find_largest_element(sample_list_one)
        print(f"Largest value in {sample_list_one}: {largest_value_one}")
    except ValueError as e:
        print(e)

    sample_list_two = [-5, -1, -10, -3]
    try:
        largest_value_two = find_largest_element(sample_list_two)
        print(f"Largest value in {sample_list_two}: {largest_value_two}")
    except ValueError as e:
        print(e)