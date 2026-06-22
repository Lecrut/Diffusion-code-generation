def get_last_item(iterable):
    last_item = None
    for item in iterable:
        last_item = item
    return last_item

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)