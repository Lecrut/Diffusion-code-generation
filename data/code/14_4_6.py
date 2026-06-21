def get_third_item(items):
    if not isinstance(items, (list, tuple)) or len(items) < 3:
        raise IndexError("List must have at least three items")
    if not all(isinstance(item, str) for item in items):
        raise TypeError("All items must be strings")
    return items[2]

if __name__ == '__main__':
    hard_coded_list = ["first", "second", "third", "fourth"]
    result = get_third_item(hard_coded_list)
    print(result)