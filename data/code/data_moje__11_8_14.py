def get_last_item(lst):
    if not lst:
        raise IndexError("List is empty")
    return [item for idx, item in enumerate(lst) if idx == len(lst) - 1][0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)