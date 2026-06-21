def combine_lists(list1, list2):
    try:
        if not isinstance(list1, list) or not isinstance(list2, list):
            raise TypeError("Both inputs must be lists.")
        return list(zip(list1, list2))
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    result = combine_lists(list_a, list_b)
    print(result)