def get_edge_elements(lst):
    if not lst:
        raise ValueError("List must not be empty")
    return (lst[0], lst[-1])

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20, 25]
    try:
        first, last = get_edge_elements(sample_list)
        print(f"First element: {first}")
        print(f"Last element: {last}")
    except ValueError as e:
        print(e)