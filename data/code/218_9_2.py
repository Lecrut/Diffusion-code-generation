def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for element in data[1:]:
        if element < minimum:
            minimum = element
    return minimum
if __name__ == '__main__':
    sample_list_1 = [3, 1, 4, 1, 5, 9, 2]
    sample_list_2 = [-10, 5, 0, -20, 15]
    sample_list_3 = [7]
    sample_list_4 = []
    print(f"List: {sample_list_1}")
    try:
        min1 = find_minimum(sample_list_1)
        print(f"Minimum element in {sample_list_1}: {min1}")
    except ValueError as e:
        print(f"Error for {sample_list_1}: {e}")
    print("-" * 20)
    print(f"List: {sample_list_2}")
    try:
        min2 = find_minimum(sample_list_2)
        print(f"Minimum element in {sample_list_2}: {min2}")
    except ValueError as e:
        print(f"Error for {sample_list_2}: {e}")
    print("-" * 20)
    print(f"List: {sample_list_3}")
    try:
        min3 = find_minimum(sample_list_3)
        print(f"Minimum element in {sample_list_3}: {min3}")
    except ValueError as e:
        print(f"Error for {sample_list_3}: {e}")
    print("-" * 20)
    print(f"List: {sample_list_4}")
    try:
        min4 = find_minimum(sample_list_4)
        print(f"Minimum element in {sample_list_4}: {min4}")
    except ValueError as e:
        print(f"Error for {sample_list_4}: {e}")