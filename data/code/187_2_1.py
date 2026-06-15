def get_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    maximum = data[0]
    for element in data[1:]:
        if element > maximum:
            maximum = element
    return maximum
if __name__ == '__main__':
    list1 = [3.14, 1.618, 2.718, 0.577]
    list2 = [-10.5, -5.2, -20.1, -1.0]
    list3 = [42.0]
    list4 = [1.0, 99.9, 50.5, 100.0]
    empty_list = []
    print(f"Maximum of {list1}: {get_maximum(list1)}")
    print(f"Maximum of {list2}: {get_maximum(list2)}")
    print(f"Maximum of {list3}: {get_maximum(list3)}")
    print(f"Maximum of {list4}: {get_maximum(list4)}")
    try:
        get_maximum(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")