def get_second_item(lst):
    if len(lst) < 2:
        return None
    return lst[1]

if __name__ == '__main__':
    SAMPLE_LIST_1 = [10, 20, 30]
    SAMPLE_LIST_2 = [5]
    SAMPLE_LIST_3 = ['a', 'b', 'c']
    SAMPLE_LIST_4 = []

    sample_lists = [SAMPLE_LIST_1, SAMPLE_LIST_2, SAMPLE_LIST_3, SAMPLE_LIST_4]

    for i, lst in enumerate(sample_lists):
        print(f"The second item in list {i+1} is: {get_second_item(lst)}")