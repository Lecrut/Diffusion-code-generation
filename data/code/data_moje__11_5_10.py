def get_last_item(items):
    last_item = None
    for item in items:
        last_item = item
    return last_item

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_last_item(sample_data)
    print(result)