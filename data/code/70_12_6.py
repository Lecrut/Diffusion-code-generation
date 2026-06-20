def get_edge_elements(lst):
    first_element = lst[0]
    last_element = lst[-1]
    return (first_element, last_element)

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 11]
    result = get_edge_elements(sample_list)
    print(f"First element: {result[0]}")
    print(f"Last element: {result[1]}")