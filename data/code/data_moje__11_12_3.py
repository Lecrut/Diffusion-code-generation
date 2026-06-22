def get_last_item(lst: list) -> any:
    if len(lst) == 0:
        return None
    return lst[len(lst) - 1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)