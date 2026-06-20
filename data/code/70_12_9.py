def get_edge_elements(lst):
    if not lst:
        raise ValueError("List must not be empty")
    first = lst[0]
    last = lst[-1]
    return (first, last)

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'd']
    result = get_edge_elements(sample_list)
    print(f"First element: {result[0]}")
    print(f"Last element: {result[1]}")