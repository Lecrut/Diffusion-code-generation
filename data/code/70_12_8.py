def get_edge_elements(lst):
    if not lst:
        return None, None
    first = lst[0]
    last = lst[-1]
    return first, last

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_edge_elements(sample_list))