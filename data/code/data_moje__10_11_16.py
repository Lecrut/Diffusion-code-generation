def get_first_item(arr):
    if not arr:
        return None
    return arr[0]

if __name__ == '__main__':
    data_set = [42, 100, 7]
    empty_set = []
    print(get_first_item(data_set))
    print(get_first_item(empty_set))