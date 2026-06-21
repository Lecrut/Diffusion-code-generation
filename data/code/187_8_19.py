def find_largest(data):
    if not data:
        return None
    largest = max(data)
    return largest

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"List: {list1}, Largest element: {find_largest(list1)}")
    list2 = [-10, -5, -20, -1]
    print(f"List: {list2}, Largest element: {find_largest(list2)}")
    list3 = [7]
    print(f"List: {list3}, Largest element: {find_largest(list3)}")
    list4 = []
    print(f"List: {list4}, Largest element: {find_largest(list4)}")