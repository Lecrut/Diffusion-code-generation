def get_last_item(items):
    if not items:
        return None
    return items[-1]

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    result = get_last_item(data)
    print(result)