from functools import reduce

def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    largest = reduce(lambda x, y: x if x > y else y, data)
    return largest

if __name__ == '__main__':
    list1 = [3, 7, 2, 8, 5]
    list2 = [-3, -7, -2, -8, -5]
    list3 = [42, 42, 42, 42, 42]
    list4 = [1]
    empty_list = []
    
    print(f"List 1: {list1}, Largest element: {find_largest(list1)}")
    print(f"List 2: {list2}, Largest element: {find_largest(list2)}")
    print(f"List 3: {list3}, Largest element: {find_largest(list3)}")
    print(f"List 4: {list4}, Largest element: {find_largest(list4)}")