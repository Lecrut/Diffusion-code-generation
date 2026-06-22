def get_edge_elements(lst):
    if len(lst) == 0:
        raise ValueError("Input must be non-empty")
    return (lst[0], lst[-1])

if __name__ == '__main__':
    data = ['a', 'b', 'c', 'd', 'e']
    print(get_edge_elements(data))