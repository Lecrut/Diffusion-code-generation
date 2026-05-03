def get_first_element(data):
    if not data:
        raise IndexError("list is empty")
    return data[0]
if __name__ == '__main__':
    list1 = [10, 20, 30]
    list2 = []
    list3 = ['a']
    try:
        result1 = get_first_element(list1)
        print(f"First element of {list1}: {result1}")
        result2 = get_first_element(list2)
        print(f"First element of {list2}: {result2}")
    except IndexError as e:
        print(f"Error for list2: {e}")
    try:
        result3 = get_first_element(list3)
        print(f"First element of {list3}: {result3}")
    except IndexError as e:
        print(f"Error for list3: {e}")