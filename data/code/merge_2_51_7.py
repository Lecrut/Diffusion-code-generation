def get_first_item(items):
    if not items:
        return None
    return items[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 'apple', True]
    result = get_first_item(sample_list)
    print(result)