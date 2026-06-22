def get_first_element(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list')
    return lst[0] if lst else None

if __name__ == '__main__':
    SAMPLE_LIST_1 = [1, 2, 3]
    SAMPLE_LIST_2 = []
    SAMPLE_LIST_3 = ['a', 'b', 'c']
    SAMPLE_LIST_4 = [True, False]
    SAMPLE_LIST_5 = [None]

    sample_data = [
        SAMPLE_LIST_1,
        SAMPLE_LIST_2,
        SAMPLE_LIST_3,
        SAMPLE_LIST_4,
        SAMPLE_LIST_5
    ]

    for data in sample_data:
        print(get_first_element(data))