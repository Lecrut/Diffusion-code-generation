def get_first_item(arr):
    return arr[0] if arr else None

if __name__ == '__main__':
    print(get_first_item([1, 2, 3]))
    print(get_first_item([]))
    print(get_first_item(['a', 'b', 'c']))
    print(get_first_item([42]))
    print(get_first_item([0, False, None, '']))