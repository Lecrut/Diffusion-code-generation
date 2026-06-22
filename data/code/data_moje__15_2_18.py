def get_second_to_last_element(lst):
    if len(lst) < 2:
        raise IndexError('List must have at least two elements')
    return lst[-2]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_second_to_last_element(sample_list)
    print(result)