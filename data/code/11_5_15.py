def get_last_item(items):
    if not items:
        raise ValueError("List is empty")
    last_item = items[0]
    for item in items:
        last_item = item
    return last_item

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)