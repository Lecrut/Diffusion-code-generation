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
    print(f"List: {list1}, Largest Absolute Value: {find_absolute_largest(list1)}")
    list2 = [-100, -50, -1, -200]
    print(f"List: {list2}, Largest Absolute Value: {find_absolute_largest(list2)}")
    list3 = [0, 0, 0, 0]
    print(f"List: {list3}, Largest Absolute Value: {find_absolute_largest(list3)}")
    list4 = [-5, 1, -10, 3]
    print(f"List: {list4}, Largest Absolute Value: {find_absolute_largest(list4)}")
    list5 = [99, -100, 50]
    print(f"List: {list5}, Largest Absolute Value: {find_absolute_largest(list5)}")