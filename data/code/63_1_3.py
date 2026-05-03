def get_first_element(data):
    if not data:
        raise IndexError("list is empty")
    return data[0]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = []
    list3 = ['a', 'b', 'c']
    try:
        result1 = get_first_element(list1)
        print(f"First element of {list1}: {result1}")
        result3 = get_first_element(list3)
        print(f"First element of {list3}: {result3}")
        get_first_element(list2)
    except IndexError as e:
        print(f"Error caught: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")