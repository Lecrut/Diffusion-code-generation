def get_edge_elements(lst):
    return (lst[0], lst[-1])

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_edge_elements(sample_list))