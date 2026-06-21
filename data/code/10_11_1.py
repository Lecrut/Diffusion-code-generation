def get_first_item(arr):
    if not arr:
        return None
    return arr[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    empty_list = []
    print(get_first_item(sample_list))
    print(get_first_item(empty_list))