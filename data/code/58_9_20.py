def get_first_element(lst):
    if not lst:
        return None
    return lst[0]

if __name__ == '__main__':
    SAMPLE_LIST = [7, 14, 21, 28]
    EMPTY_LIST = []
    print(get_first_element(SAMPLE_LIST))
    print(get_first_element(EMPTY_LIST))