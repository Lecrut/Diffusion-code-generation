def get_last_item_pop(items):
    if len(items) == 0:
        return None
    return items.pop()

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_last_item_pop(sample_list)
    print(result)
    print(get_last_item_pop([]))