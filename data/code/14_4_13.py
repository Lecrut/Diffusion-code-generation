def get_third_item(items):
    if not isinstance(items, (list, tuple)):
        raise TypeError("Expected a list or tuple")
    if len(items) < 3:
        raise IndexError("List must have at least three items")
    return items[2]

if __name__ == '__main__':
    sample_list = ["first", "second", "third", "fourth"]
    result = get_third_item(sample_list)
    print(result)