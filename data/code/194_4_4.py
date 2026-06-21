def find_longest_list_item(lst):
    if not lst:
        return None
    try:
        longest = max(lst, key=len)
    except TypeError as e:
        raise ValueError("List contains non-comparable items") from e
    return longest

if __name__ == '__main__':
    sample_list = [[1], [2, 3], [4, 5, 6], [], [7, 8, 9, 10]]
    result = find_longest_list_item(sample_list)
    print(result)