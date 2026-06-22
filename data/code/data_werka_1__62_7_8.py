def find_second_element(lst):
    if len(lst) < 2:
        return None
    elif len(lst) == 2:
        return lst[1]
    else:
        return find_second_element(lst[1:])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(find_second_element(sample_list))