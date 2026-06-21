def get_first_item(arr):
    if not arr:
        return None
    return arr[0]

if __name__ == '__main__':
    print(get_first_item([1, 2, 3]))
    print(get_first_item([]))
    print(get_first_item(['a', 'b', 'c']))
    print(get_first_item([None]))