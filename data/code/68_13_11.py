def find_unique_items(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    set1 = set(list1)
    set2 = set(list2)
    unique_items = set1.difference(set2)
    return list(unique_items)

if __name__ == '__main__':
    SAMPLE_LIST_1 = [100, 200, 300, 400, 500]
    SAMPLE_LIST_2 = [400, 500, 600, 700, 800]
    try:
        unique_items = find_unique_items(SAMPLE_LIST_1, SAMPLE_LIST_2)
        print(unique_items)
    except ValueError as e:
        print(e)