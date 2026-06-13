def find_absolute_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for x in data:
        if x > largest:
            largest = x
    return largest
if __name__ == '__main__':
    list1 = [5, -2, 8, -10, 3]
    print(f"List: {list1}, Absolute Largest: {find_absolute_largest(list1)}")
    list2 = [-1, -5, -2, -10]
    print(f"List: {list2}, Absolute Largest: {find_absolute_largest(list2)}")
    list3 = [0, 0, 0]
    print(f"List: {list3}, Absolute Largest: {find_absolute_largest(list3)}")
    list4 = [100, -50, 75, -200]
    print(f"List: {list4}, Absolute Largest: {find_absolute_largest(list4)}")
    list5 = [-5, 10, -1, 3]
    print(f"List: {list5}, Absolute Largest: {find_absolute_largest(list5)}")