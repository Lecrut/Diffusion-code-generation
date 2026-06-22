def find_largest_item(items: list) -> int:
    if not items:
        raise ValueError("List is empty")
    largest = max(items)
    return largest

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_largest_item(sample_list))