def get_last_item(lst):
    if not lst:
        raise ValueError("List is empty")
    max_index = max(range(len(lst)))
    return [item for index, item in enumerate(lst) if index == max_index][0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)