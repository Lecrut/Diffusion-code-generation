from functools import reduce

def find_largest_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return reduce(lambda x, y: x if x > y else y, data)

if __name__ == '__main__':
    list1 = [10, 5, 20, 8, 15]
    list2 = [-5, -1, -10, -2]
    list3 = [7, 7, 7, 7]
    list4 = [42]
    list5 = [-100, 0, -50]
    empty_list = []
    try:
        print(f"List 1: {list1}, Largest element: {find_largest_element(list1)}")
        print(f"List 2: {list2}, Largest element: {find_largest_element(list2)}")
        print(f"List 3: {list3}, Largest element: {find_largest_element(list3)}")
        print(f"List 4: {list4}, Largest element: {find_largest_element(list4)}")
        print(f"List 5: {list5}, Largest element: {find_largest_element(list5)}")
    except ValueError as e:
        print(e)