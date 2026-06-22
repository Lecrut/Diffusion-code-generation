def get_last_element(items):
    if not items:
        return None
    last_index = len(items) - 1
    return items[last_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_element(sample_list)
    print(result)