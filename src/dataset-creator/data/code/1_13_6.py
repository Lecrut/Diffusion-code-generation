def has_valid_item(collection):
    return any(item > 50 for item in collection) if isinstance(collection, list) else False
if __name__ == '__main__':
    data = [12, 48, 67, 34]
    result = has_valid_item(data)
    print(result)