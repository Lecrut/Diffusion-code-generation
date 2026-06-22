def find_largest_item(items: list) -> float:
    if not items:
        raise ValueError("List is empty")
    max_item = float('-inf')
    for item in items:
        if item > max_item:
            max_item = item
    return max_item

if __name__ == '__main__':
    sample_list = [3, 5.5, 1, 2, 4]
    print(find_largest_item(sample_list))