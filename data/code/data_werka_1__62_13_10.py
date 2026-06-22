def safe_second_element(lst):
    MIN_LENGTH = 2
    if len(lst) < MIN_LENGTH:
        return None
    return lst[1]

if __name__ == '__main__':
    SAMPLE_LIST_1 = [100, 200, 300]
    SAMPLE_LIST_2 = ['x']
    SAMPLE_LIST_3 = []
    print(safe_second_element(SAMPLE_LIST_1))
    print(safe_second_element(SAMPLE_LIST_2))
    print(safe_second_element(SAMPLE_LIST_3))