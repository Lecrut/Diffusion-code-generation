def compare_elements(data, index1, index2):
    if not (0 <= index1 < len(data) and 0 <= index2 < len(data)):
        raise IndexError("Index out of bounds")
    val1 = data[index1]
    val2 = data[index2]
    if val1 > val2:
        return 'greater than'
    elif val1 < val2:
        return 'less than'
    else:
        return 'equal'
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(f"Comparing elements at index 1 and 3: {compare_elements(sample_list, 1, 3)}")
    print(f"Comparing elements at index 0 and 4: {compare_elements(sample_list, 0, 4)}")
    print(f"Comparing elements at index 2 and 2: {compare_elements(sample_list, 2, 2)}")
    print(f"Comparing elements at index 4 and 1: {compare_elements(sample_list, 4, 1)}")
    try:
        compare_elements(sample_list, 0, 5)
    except IndexError as e:
        print(f"Error caught: {e}")
    try:
        compare_elements(sample_list, -1, 2)
    except IndexError as e:
        print(f"Error caught: {e}")