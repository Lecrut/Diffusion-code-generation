def get_first_element(data):
    try:
        return data[0]
    except IndexError:
        raise ValueError("Input list cannot be empty")

if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = ['a', 'b', 'c']
    empty_list = []
    try:
        print(f"First element of {list1}: {get_first_element(list1)}")
        print(f"First element of {list2}: {get_first_element(list2)}")
        get_first_element(empty_list)
    except ValueError as e:
        print(f"Caught expected error: {e}")