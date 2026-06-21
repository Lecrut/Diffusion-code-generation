def zip_lists(list1, list2):
    try:
        if not isinstance(list1, list) or not isinstance(list2, list):
            raise TypeError("Both inputs must be lists.")
        return list(zip(list1, list2))
    except TypeError as e:
        return [f"Error: {e}"]

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    result = zip_lists(list_a, list_b)
    print(f"Zipped lists of {list_a} and {list_b}: {result}")