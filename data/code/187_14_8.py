def find_largest_element(data):
    if not data:
        raise ValueError("Cannot find largest element in an empty list.")
    return max(data)

if __name__ == '__main__':
    sample_list_one = [10, 5, 20, 8]
    try:
        largest_val_one = find_largest_element(sample_list_one)
        print(f"The largest value in {sample_list_one} is: {largest_val_one}")
    except ValueError as e:
        print(f"Error for sample list one: {e}")

    sample_list_two = [-5, -1, -10]
    try:
        largest_val_two = find_largest_element(sample_list_two)
        print(f"The largest value in {sample_list_two} is: {largest_val_two}")
    except ValueError as e:
        print(f"Error for sample list two: {e}")