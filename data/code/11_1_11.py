def get_last_item_pop(data):
    if not data:
        return None
    return data.pop()

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_last_item_pop(sample_list)
    print(result)
    print(get_last_item_pop([]))