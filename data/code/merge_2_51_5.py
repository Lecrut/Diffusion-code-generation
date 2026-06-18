def find_initial_item(items):
    if not items:
        raise ValueError("List cannot be empty")
    return items[0]
if __name__ == '__main__':
    sample_list = [1, 2, "apple", None, True]
    result = find_initial_item(sample_list)
    print(result)