def get_first_item(array):
    if not array:
        return None
    return array[0]

if __name__ == '__main__':
    print(get_first_item([1, 2, 3]))
    print(get_first_item([]))