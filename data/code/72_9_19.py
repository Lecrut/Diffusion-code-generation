def compare_elements(lst, idx1, idx2):
    try:
        elem1 = lst[idx1]
        elem2 = lst[idx2]
        if elem1 > elem2:
            return 'greater than'
        elif elem1 < elem2:
            return 'less than'
        else:
            return 'equal'
    except IndexError:
        return 'index out of bounds'
if __name__ == '__main__':
    sample_list = [5, 3, 9, 1]
    print(compare_elements(sample_list, 0, 2))
    print(compare_elements(sample_list, 1, 3))
    print(compare_elements(sample_list, 2, 2))
    print(compare_elements(sample_list, 4, 1))