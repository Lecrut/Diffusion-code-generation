def fetch_edge_elements(iterable):
    try:
        first = iterable[0]
        last = iterable[-1]
    except IndexError:
        return None, None
    return first, last

if __name__ == '__main__':
    sample_list1 = [23, 45, 67, 89, 101]
    sample_list2 = ['apple', 'banana']
    sample_list3 = []
    
    print(f"List 1: {fetch_edge_elements(sample_list1)}")
    print(f"List 2: {fetch_edge_elements(sample_list2)}")
    print(f"List 3: {fetch_edge_elements(sample_list3)}")