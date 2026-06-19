def find_final_item_index(lst, item):
    try:
        return lst.index(item)
    except ValueError:
        return -1

if __name__ == '__main__':
    test_cases = [
        ([], 5),
        ([1, 2, 3, 4, 5], 5),
        ([1, 2, 3, 4, 5], 6),
        (['a', 'b', 'c', 'd'], 'c'),
        (['a', 'b', 'c', 'd'], 'e')
    ]

    for i, (lst, item) in enumerate(test_cases):
        result = find_final_item_index(lst, item)
        print(f"Test case {i+1}: List = {lst}, Item = {item}, Index = {result}")