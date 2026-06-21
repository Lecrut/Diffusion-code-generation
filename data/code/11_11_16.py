def get_final_item(lst):
    if len(lst) == 0:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_final_item(sample_list)
    print(result)
    empty_list = []
    result_empty = get_final_item(empty_list)
    print(result_empty)