from functools import reduce

def find_largest_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return reduce(lambda x, y: x if x > y else y, data)

if __name__ == '__main__':
    sample_list1 = [34, 78, 12, 90, 56]
    sample_list2 = [-10, -20, -30, -40, -50]
    sample_list3 = [100, 100, 100, 100]

    print(f"List 1: {sample_list1}, Largest element: {find_largest_element(sample_list1)}")
    print(f"List 2: {sample_list2}, Largest element: {find_largest_element(sample_list2)}")
    print(f"List 3: {sample_list3}, Largest element: {find_largest_element(sample_list3)}")