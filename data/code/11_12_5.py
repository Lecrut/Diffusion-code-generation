def get_last_item(lst: list) -> object:
    return lst[len(lst) - 1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)