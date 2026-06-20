def get_edge_elements(lst):
    return (lst[0], lst[-1])

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10]
    first_element, last_element = get_edge_elements(sample_list)
    print(f"First element: {first_element}")
    print(f"Last element: {last_element}")