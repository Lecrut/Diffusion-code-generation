def get_last_item(items):
    last = None
    for item in items:
        last = item
    return last

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_last_item(sample_list)
    print(result)