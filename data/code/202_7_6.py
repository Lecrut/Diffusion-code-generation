def find_absolute_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for x in data:
        if x > largest:
            largest = x
    return largest
if __name__ == '__main__':
    list1 = [5, -10, 3, 0, -8]
    result1 = find_absolute_largest(list1)
    print(f"List: {list1}, Absolute Largest: {result1}")
    list2 = [-50, -100, -5, -1]
    result2 = find_absolute_largest(list2)
    print(f"List: {list2}, Absolute Largest: {result2}")
    list3 = [10, 20, 30]
    result3 = find_absolute_largest(list3)
    print(f"List: {list3}, Absolute Largest: {result3}")
    list4 = [0, 0, 0]
    result4 = find_absolute_largest(list4)
    print(f"List: {list4}, Absolute Largest: {result4}")
    list5 = [-1, -5, -2]
    result5 = find_absolute_largest(list5)
    print(f"List: {list5}, Absolute Largest: {result5}")