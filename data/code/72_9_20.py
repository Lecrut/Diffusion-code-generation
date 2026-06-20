def compare_elements(lst, idx1, idx2):
    try:
        element1 = lst[idx1]
        element2 = lst[idx2]
        if element1 > element2:
            return 'greater than'
        elif element1 < element2:
            return 'less than'
        else:
            return 'equal'
    except IndexError:
        return 'Index out of bounds'
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(compare_elements(sample_list, 1, 3))
    print(compare_elements(sample_list, 2, 2))
    print(compare_elements(sample_list, 0, 5))