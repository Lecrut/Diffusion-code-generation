def get_first_element(lst):
    if lst:
        return lst[0]
    return None

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_first_element(sample_list)
    print(result)