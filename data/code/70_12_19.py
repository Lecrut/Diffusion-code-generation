def get_edge_elements(lst):
    first = lst[0]
    last = lst[-1]
    return first, last

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    first, last = get_edge_elements(sample_list)
    print(f"First element: {first}")
    print(f"Last element: {last}")