def get_third_item(items):
    try:
        return items[2]
    except IndexError:
        return None

if __name__ == '__main__':
    data = [10, 20, 30, 40, 50]
    print(get_third_item(data))