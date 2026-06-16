def has_valid_item(collection):
    return any(item > 0 for item in collection) if isinstance(collection, list) else False
if __name__ == '__main__':
    data = [3, -1, 5]
    result = has_valid_item(data)