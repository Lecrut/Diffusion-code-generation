def find_initial_item(items):
    return items[0] if len(items) > 0 else None
if __name__ == '__main__':
    sample_list = [1, "apple", True, {"key": "value"}]
    result = find_initial_item(sample_list)
    print(result)