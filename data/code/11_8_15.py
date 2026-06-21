def get_last_item(lst):
    if not lst:
        raise ValueError("List is empty")
    max_index = len(lst) - 1
    return [item for index, item in enumerate(lst) if index == max_index][0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)