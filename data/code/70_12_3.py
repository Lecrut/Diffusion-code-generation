def get_edge_elements(lst):
    if not lst:
        raise ValueError("List must not be empty")
    return (lst[0], lst[-1])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_edge_elements(sample_list))