def find_second_element(lst):
    if len(lst) < 2:
        return None
    elif len(lst) == 2:
        return lst[1]
    else:
        return find_second_element(lst[1:])

if __name__ == '__main__':
    sample_list = [3, 5, 7, 9, 11]
    print(find_second_element(sample_list))