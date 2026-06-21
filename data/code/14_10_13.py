def get_third_element(lst):
    if len(lst) < 3:
        return None
    return lst[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_third_element(sample_list)
    print(result)