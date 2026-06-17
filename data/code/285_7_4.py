def compare_adjacent_elements(data):
    for i in range(len(data) - 1):
        type1 = type(data[i])
        type2 = type(data[i+1])
        if type1 != type2:
            raise TypeError("Incompatible type comparison attempted between adjacent elements.")
if __name__ == '__main__':
    list1 = [1, 2.5, 3, 4.7]
    list2 = [10, 20, 30]
    list3 = [1.1, 1.2, "error"]
    list4 = [5, 6, 7]
    try:
        print("Testing list1:")
        compare_adjacent_elements(list1)
        print("List1 comparison successful.")
    except TypeError as e:
        print(f"Caught error for list1: {e}")
    try:
        print("\nTesting list2:")
        compare_adjacent_elements(list2)
        print("List2 comparison successful.")
    except TypeError as e:
        print(f"Caught error for list2: {e}")
    try:
        print("\nTesting list3:")
        compare_adjacent_elements(list3)
        print("List3 comparison successful.")
    except TypeError as e:
        print(f"Caught error for list3: {e}")
    try:
        print("\nTesting list4:")
        compare_adjacent_elements(list4)
        print("List4 comparison successful.")
    except TypeError as e:
        print(f"Caught error for list4: {e}")