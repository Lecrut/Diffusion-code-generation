def get_first_element(lst):
    LIST_TYPE = list
    NONE_VALUE = None
    
    if not isinstance(lst, LIST_TYPE):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        return NONE_VALUE
    return lst[0]

if __name__ == '__main__':
    SAMPLE_DATA = [
        [1, 2, 3],
        [],
        ['a', 'b', 'c'],
        [True, False],
        [None]
    ]
    
    for data in SAMPLE_DATA:
        print(get_first_element(data))