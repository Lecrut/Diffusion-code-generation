def get_last_item(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_last_item(sample_list)
    print(result)
    sample_list = []
    result = get_last_item(sample_list)
    print(result)