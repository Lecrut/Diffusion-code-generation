def has_valid_item(items):
    return any(item > 10 for item in items) if isinstance(items, list) else False
if __name__ == '__main__':
    data = [5, 3, 8, 20, 4]
    print(has_valid_item(data))