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
    list1 = [10, 20, 30, 40, 50]
    list2 = [5, 15, 25, 35, 45]
    print(f"Comparing list1[{0}] ({list1[0]}) and list2[{0}] ({list2[0]}): {compare_elements(list1, 0, 0)}")
    print(f"Comparing list1[1] ({list1[1]}) and list2[1] ({list2[1]}): {compare_elements(list1, 1, 1)}")
    print(f"Comparing list1[2] ({list1[2]}) and list2[3] ({list2[3]}): {compare_elements(list1, 2, 3)}")
    print(f"Comparing list1[4] ({list1[4]}) and list2[4] ({list2[4]}): {compare_elements(list1, 4, 4)}")
    print(f"Comparing list1[0] ({list1[0]}) and list2[4] ({list2[4]}): {compare_elements(list1, 0, 4)}")
    try:
        compare_elements(list1, 5, 0)
    except IndexError as e:
        print(f"Caught expected error: {e}")
    try:
        compare_elements(list1, -1, 0)
    except IndexError as e:
        print(f"Caught expected error: {e}")