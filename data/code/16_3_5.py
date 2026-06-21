def get_first_item(items):
    if not items:
        raise IndexError("Cannot get first item from an empty list")
    return items[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_first_item(sample_list)
    print(result)