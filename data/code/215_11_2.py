def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for x in data[1:]:
        if x > largest:
            largest = x
    return largest
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"The largest in {list1} is: {find_largest(list1)}")
    list2 = [-10, -5, -20, -1]
    print(f"The largest in {list2} is: {find_largest(list2)}")
    list3 = [42]
    print(f"The largest in {list3} is: {find_largest(list3)}")
    list4 = [100, 50, 200, 150]
    print(f"The largest in {list4} is: {find_largest(list4)}")