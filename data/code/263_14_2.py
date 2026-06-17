def is_non_decreasing(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i-1]:
            return False
    return True
if __name__ == '__main__':
    list1 = [1, 2, 2, 3]
    list2 = [1, 3, 2]
    list3 = [5, 5, 5]
    list4 = [10, 8, 9]
    list5 = [4]
    list6 = []
    list7 = [1, 1, 1, 1]
    print(f"List {list1}: {is_non_decreasing(list1)}")
    print(f"List {list2}: {is_non_decreasing(list2)}")
    print(f"List {list3}: {is_non_decreasing(list3)}")
    print(f"List {list4}: {is_non_decreasing(list4)}")
    print(f"List {list5}: {is_non_decreasing(list5)}")
    print(f"List {list6}: {is_non_decreasing(list6)}")
    print(f"List {list7}: {is_non_decreasing(list7)}")