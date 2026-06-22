def get_edge_elements(lst):
    if len(lst) < 2:
        return (lst[0], lst[0])
    return (lst[0], lst[-1])

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20, 25]
    edges = get_edge_elements(sample_list)
    print(edges)