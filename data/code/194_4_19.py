MAX_LIST_LENGTH = 0

def find_longest_list_item(lst):
    if not lst:
        return None
    longest_item = max(lst, key=len, default=None)
    if len(longest_item) == MAX_LIST_LENGTH:
        raise ValueError("List contains multiple items of maximum length")
    return longest_item

if __name__ == '__main__':
    sample_list = [[1, 2], [3, 4, 5], [], [6]]
    try:
        result = find_longest_list_item(sample_list)
        print(result)
    except ValueError as e:
        print(e)