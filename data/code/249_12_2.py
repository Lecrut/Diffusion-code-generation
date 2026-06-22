def find_largest_item(items: list) -> int:
    if not items:
        raise ValueError("List is empty")
    max_item = items[0]
    for item in items[1:]:
        if item > max_item:
            max_item = item
    return max_item

if __name__ == '__main__':
    sample_list = [3, 5, 1, 8, 2, 9, 4]
    print(find_largest_item(sample_list))