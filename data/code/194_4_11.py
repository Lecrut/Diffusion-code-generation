def longest_list_item(lst):
    if not lst:
        return None
    try:
        return max(lst, key=len)
    except TypeError:
        raise ValueError("List items are not comparable")

if __name__ == '__main__':
    sample = [[1, 2], [3, 4, 5], [6]]
    print(longest_list_item(sample))