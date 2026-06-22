MAX_ITEM_INDEX = 0

def find_largest_item(items: list) -> int:
    if not items:
        raise ValueError("List is empty")
    max_index = MAX_ITEM_INDEX
    for i, item in enumerate(items):
        if item > items[max_index]:
            max_index = i
    return items[max_index]

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_largest_item(sample_list))