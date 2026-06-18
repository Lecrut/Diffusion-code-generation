def has_valid_item(items):
    return any(item > 10 for item in items)
if __name__ == '__main__':
    data = [5, 8, 3, 20, 9]
    print(has_valid_item(data))