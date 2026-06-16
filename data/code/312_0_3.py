import random
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
    print(f"List: {list1}, Largest element: {find_largest(list1)}")
    list2 = [-10, -5, -20, -1]
    print(f"List: {list2}, Largest element: {find_largest(list2)}")
    list3 = [42]
    print(f"List: {list3}, Largest element: {find_largest(list3)}")
    list4 = [100, 50, 200, 10]
    print(f"List: {list4}, Largest element: {find_largest(list4)}")