def get_last_item(lst):
    return [item for i, item in enumerate(lst) if i == len(lst) - 1][-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)