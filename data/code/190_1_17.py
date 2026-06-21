def list_contains_item(data, item):
    return item in data

if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    target_item = 5
    result = list_contains_item(sample_list, target_item)
    print(f"Does {target_item} exist in the list? {result}")