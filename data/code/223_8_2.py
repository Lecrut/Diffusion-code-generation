def find_maximum(data_list):
    if not data_list:
        raise ValueError("Input list cannot be empty.")
    maximum = data_list[0]
    for element in data_list:
        if element > maximum:
            maximum = element
    return maximum
if __name__ == '__main__':
    sample_list_1 = [10, 4, 25, 8, 30]
    sample_list_2 = [-5, -1, -10, -2]
    sample_list_3 = [7]
    sample_list_4 = []
    print(f"List 1: {sample_list_1}")
    try:
        max1 = find_maximum(sample_list_1)
        print(f"Maximum of List 1: {max1}")
    except ValueError as e:
        print(f"Error for List 1: {e}")
    print(f"\nList 2: {sample_list_2}")
    try:
        max2 = find_maximum(sample_list_2)
        print(f"Maximum of List 2: {max2}")
    except ValueError as e:
        print(f"Error for List 2: {e}")
    print(f"\nList 3: {sample_list_3}")
    try:
        max3 = find_maximum(sample_list_3)
        print(f"Maximum of List 3: {max3}")
    except ValueError as e:
        print(f"Error for List 3: {e}")
    print(f"\nList 4: {sample_list_4}")
    try:
        max4 = find_maximum(sample_list_4)
        print(f"Maximum of List 4: {max4}")
    except ValueError as e:
        print(f"Error for List 4: {e}")