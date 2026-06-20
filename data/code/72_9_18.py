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
        return 'index out of bounds'
if __name__ == '__main__':
    sample_list = [5, 3, 9, 7, 1]
    result = compare_elements(sample_list, 2, 4)
    print(result)