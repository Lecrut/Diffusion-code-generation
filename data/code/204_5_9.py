def find_middle_value(lst):
    lst.sort()
    length = len(lst)
    if length % 2 == 0:
        return (lst[length // 2 - 1] + lst[length // 2]) / 2
    else:
        return lst[length // 2]

if __name__ == '__main__':
    sample_list = [7, 3, 5, 9, 1]
    print("Original list:", sample_list)
    middle_value = find_middle_value(sample_list)
    print("Middle value:", middle_value)

    another_list = [8, 2, 6, 4]
    print("\nOriginal list:", another_list)
    another_middle_value = find_middle_value(another_list)
    print("Middle value:", another_middle_value)