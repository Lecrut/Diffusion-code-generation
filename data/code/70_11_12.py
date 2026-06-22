def get_edge_elements(lst):
    if not hasattr(lst, '__len__'):
        raise ValueError("Input must be a sequence")
    if len(lst) < 1:
        raise ValueError("Input must be non-empty")
    return (lst[0], lst[-1])

if __name__ == '__main__':
    test_list = [100, 200, 300, 400, 500]
    result = get_edge_elements(test_list)
    print(result)