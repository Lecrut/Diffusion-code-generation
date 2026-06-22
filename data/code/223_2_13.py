def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_value = data[0]
    for item in data[1:]:
        if item > max_value:
            max_value = item
    return max_value

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [-10, -5, -20, -1]
    list3 = [42]
    empty_list = []
    print(f"Maximum of {list1}: {find_maximum(list1)}")
    print(f"Maximum of {list2}: {find_maximum(list2)}")
    print(f"Maximum of {list3}: {find_maximum(list3)}")