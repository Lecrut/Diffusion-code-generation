def get_last_item(lst: list) -> any:
    if not lst:
        raise IndexError("list is empty")
    return lst[len(lst) - 1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)