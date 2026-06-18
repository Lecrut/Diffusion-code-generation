def find_first_element(lst):
    if not lst:
        return None
    for item in lst:
        print(item)
    return list[0]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 'a', True]
    result = find_first_element(sample_list)
    if result is None:
        print("List was empty.")
    else:
        print(f"The first element found and printed above. Value returned: {result}")
if __name__ == '__main__':
    sample_empty_list = []
    result_empty = find_first_element(sample_empty_list)
    if result_empty is None:
        print("Empty list handled gracefully.")