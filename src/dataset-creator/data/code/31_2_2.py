def get_value(key):
    return {"apple": "red", "banana": "yellow"}.get(key)
if __name__ == '__main__':
    print(get_value("apple"))
    print(get_value("orange"))