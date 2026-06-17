def compare_adjacent(data):
    for i in range(len(data) - 1):
        type1 = type(data[i])
        type2 = type(data[i+1])
        if type1 != type2:
            raise TypeError("Incompatible type comparison attempted between adjacent elements.")
if __name__ == '__main__':
    list1 = [1, 2.5, 3, 4.7]
    list2 = [10, 20, 30]
    list3 = [1, 2, 'a', 4]
    list4 = [1.0, 2.0, 3.0]
    print("Testing list1:")
    try:
        compare_adjacent(list1)
        print("List1 comparison successful.")
    except TypeError as e:
        print(f"Error for List1: {e}")
    print("\nTesting list2:")
    try:
        compare_adjacent(list2)
        print("List2 comparison successful.")
    except TypeError as e:
        print(f"Error for List2: {e}")
    print("\nTesting list3:")
    try:
        compare_adjacent(list3)
        print("List3 comparison successful.")
    except TypeError as e:
        print(f"Error for List3: {e}")
    print("\nTesting list4:")
    try:
        compare_adjacent(list4)
        print("List4 comparison successful.")
    except TypeError as e:
        print(f"Error for List4: {e}")