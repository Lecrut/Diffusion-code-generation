def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = []
    list3 = [-10, -5, -20]

    result1 = find_largest(list1)
    print(f"The largest element in {list1} is: {result1}")

    result2 = find_largest(list2)
    print(f"The largest element in {list2} is: {result2 if result2 is not None else 'Empty list'}")

    result3 = find_largest(list3)
    print(f"The largest element in {list3} is: {result3}")