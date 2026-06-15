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
    list2 = [-10.5, -5.2, -20.1, -1.9]
    list3 = [42.0, 100.5, 5.5, 99.9]
    list4 = [7.7]
    list5 = []
    print(f"Maximum of {list1}: {get_maximum(list1)}")
    print(f"Maximum of {list2}: {get_maximum(list2)}")
    print(f"Maximum of {list3}: {get_maximum(list3)}")
    print(f"Maximum of {list4}: {get_maximum(list4)}")
    try:
        print(f"Maximum of {list5}: {get_maximum(list5)}")
    except ValueError as e:
        print(f"Error for {list5}: {e}")