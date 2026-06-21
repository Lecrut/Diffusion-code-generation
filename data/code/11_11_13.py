def pop_last_item(lst):
    if not lst:
        return None
    return lst.pop()

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = []
    result_1 = pop_last_item(sample_list_1)
    result_2 = pop_last_item(sample_list_2)
    print(result_1)
    print(result_2)