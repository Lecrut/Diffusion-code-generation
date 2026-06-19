def get_first_element(lst):
    return lst[0] if lst else None

if __name__ == '__main__':
    SAMPLE_LIST = [7, 14, 21]
    print(get_first_element(SAMPLE_LIST))