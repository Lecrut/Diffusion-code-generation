def get_first_item(array):
    try:
        return array[0]
    except (IndexError, TypeError):
        return None

if __name__ == '__main__':
    data = [1, 2, 3]
    print(get_first_item(data))
    print(get_first_item([]))
    print(get_first_item(None))
    print(get_first_item([42]))