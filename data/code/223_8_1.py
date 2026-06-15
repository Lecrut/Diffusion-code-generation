def find_maximum(data_list):
    if not data_list:
        raise ValueError("Input list cannot be empty.")
    maximum = data_list[0]
    for element in data_list:
        if element > maximum:
            maximum = element
    return maximum
if __name__ == '__main__':
    sample_list_1 = [10, 5, 20, 8, 15]
    sample_list_2 = [-5, -1, -10, -3]
    sample_list_3 = [42]
    sample_list_4 = []
    print(f"List 1: {sample_list_1}")
    try:
        max1 = find_maximum(sample_list_1)
        print(f"Maximum of List 1: {max1}\n")
    except ValueError as e:
        print(f"Error for List 1: {e}\n")
    print(f"List 2: {sample_list_2}")
    try:
        max2 = find_maximum(sample_list_2)
        print(f"Maximum of List 2: {max2}\n")
    except ValueError as e:
        print(f"Error for List 2: {e}\n")
    print(f"List 3: {sample_list_3}")
    try:
        max3 = find_maximum(sample_list_3)
        print(f"Maximum of List 3: {max3}\n")
    except ValueError as e:
        print(f"Error for List 3: {e}\n")
    print(f"List 4: {sample_list_4}")
    try:
        max4 = find_maximum(sample_list_4)
        print(f"Maximum of List 4: {max4}\n")
    except ValueError as e:
        print(f"Error for List 4: {e}\n")