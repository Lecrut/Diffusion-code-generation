def get_edge_elements(lst):
    if not isinstance(lst, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(lst) == 0:
        raise ValueError("Input must be non-empty")
    
    edge_map = {
        'first': 0,
        'last': -1
    }
    
    first_index = edge_map['first']
    last_index = edge_map['last']
    
    return (lst[first_index], lst[last_index])

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    output = get_edge_elements(sample_data)
    print(output)