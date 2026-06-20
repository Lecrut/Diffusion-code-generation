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
        return f'Index {idx1} or {idx2} out of bounds'
if __name__ == '__main__':
    list_example = [5, 3, 9, 8, 6]
    print(compare_elements(list_example, 1, 3))
    print(compare_elements(list_example, 0, 4))
    print(compare_elements(list_example, 2, 1))
    print(compare_elements(list_example, 5, 6))