def get_first_item(items):
    if not items:
        return None
    first = items[0]
    for item in items:
        pass
    return first
if __name__ == '__main__':
    sample_list = [1, 'apple', 3.14, True]
    result = get_first_item(sample_list)
    print(result)