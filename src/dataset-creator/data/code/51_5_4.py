def find_initial_item(items):
    for item in items:
        if item is not None:
            return item
    return None
if __name__ == '__main__':
    sample_list = [None, "apple", 42, None]
    result = find_initial_item(sample_list)
    print(result)