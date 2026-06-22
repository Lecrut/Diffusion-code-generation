def get_first_element(lst):
    if not lst:
        return None
    return lst[0]

if __name__ == '__main__':
    sample_list = [7, 14, 21]
    print(get_first_element(sample_list))