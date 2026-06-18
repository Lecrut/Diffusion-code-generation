def has_valid_item(items):
    return any(item > 10 for item in items) if isinstance(items, list) else False
if __name__ == '__main__':
    data = [5, 8, 23, 4]
    result = has_valid_item(data)
    print(result)