def binary_search(data_list, element):
    low = 0
    high = len(data_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if data_list[mid] == element:
            return True
        elif data_list[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return False

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    element1 = 8
    print(f"List: {list1}, Element: {element1}, Result: {binary_search(sorted(list1), element1)}")
    list2 = ['a', 'b', 'c']
    element2 = 'd'
    print(f"List: {list2}, Element: {element2}, Result: {binary_search(sorted(list2), element2)}")
    list3 = [10, 20, 30]
    element3 = 20
    print(f"List: {list3}, Element: {element3}, Result: {binary_search(sorted(list3), element3)}")