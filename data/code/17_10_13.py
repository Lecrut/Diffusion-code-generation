def get_last_item(items):
    if not items:
        return None
    return items[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_item(sample_list))
    print(get_last_item([]))
    print(get_last_item([42]))