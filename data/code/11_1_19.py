def get_last_item(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_last_item(sample_list)
    print(result)

    empty_list = []
    empty_result = get_last_item(empty_list)
    print(empty_result)