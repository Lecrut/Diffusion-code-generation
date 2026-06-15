def find_absolute_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for x in data:
        if x > largest:
            largest = x
    return largest
if __name__ == '__main__':
    list1 = [5, -10, 3, -8, 0]
    print(f"List: {list1}, Absolute Largest: {find_absolute_largest(list1)}")
    list2 = [-50, -100, -5]
    print(f"List: {list2}, Absolute Largest: {find_absolute_largest(list2)}")
    list3 = [1, 2, 3, 4, 5]
    print(f"List: {list3}, Absolute Largest: {find_absolute_largest(list3)}")
    list4 = [0, 0, 0, -1, -5]
    print(f"List: {list4}, Absolute Largest: {find_absolute_largest(list4)}")
    list5 = [-10, 20, -5, 15]
    print(f"List: {list5}, Absolute Largest: {find_absolute_largest(list5)}")