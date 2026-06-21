def get_last_item(items):
    last = None
    for item in items:
        last = item
    return last

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)