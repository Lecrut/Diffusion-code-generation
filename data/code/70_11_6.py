def get_edge_elements(lst):
    return (lst[0], lst[-1])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_edge_elements(sample_list)
    print(result)