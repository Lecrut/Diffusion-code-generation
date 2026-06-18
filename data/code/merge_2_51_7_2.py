def get_leading_item(items):
    return items[0] if items else None
if __name__ == '__main__':
    data = [10, 20, 30, 40]
    result = get_leading_item(data)
    print(result)