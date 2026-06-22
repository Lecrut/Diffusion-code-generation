def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest

if __name__ == '__main__':
    sample_lists = {
        "list1": [1, 5, 2, 8, 3],
        "list2": [-10, -5, -20, -1],
        "list3": [42],
        "list4": [3.14, 2.71, 1.618]
    }

    for name, lst in sample_lists.items():
        print(f"List: {lst}, Largest: {find_largest(lst)}")