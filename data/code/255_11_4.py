def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = data[0]
    for x in data[1:]:
        if x > max_val:
            max_val = x
    return max_val
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, -5, -20, -1]
    list3 = [7]
    list4 = []
    print(f"Maximum of {list1}: {find_maximum(list1)}")
    print(f"Maximum of {list2}: {find_maximum(list2)}")
    print(f"Maximum of {list3}: {find_maximum(list3)}")
    try:
        print(f"Maximum of {list4}: {find_maximum(list4)}")
    except ValueError as e:
        print(f"Error for {list4}: {e}")