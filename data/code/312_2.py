def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest
if __name__ == '__main__':
    list1 = [10, 5, 20, 8, 15]
    print(f"The largest element in {list1} is: {find_largest(list1)}")
    list2 = [-5, -1, -10, -3]
    print(f"The largest element in {list2} is: {find_largest(list2)}")
    list3 = [42]
    print(f"The largest element in {list3} is: {find_largest(list3)}")
    list4 = [100, 50, 25, 75]
    print(f"The largest element in {list4} is: {find_largest(list4)}")