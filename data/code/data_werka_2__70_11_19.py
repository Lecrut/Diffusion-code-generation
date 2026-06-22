EDGE_FIRST_INDEX = 0
EDGE_LAST_INDEX = -1

def get_edge_elements(lst):
    if not lst:
        raise ValueError("Input list must not be empty")
    return (lst[EDGE_FIRST_INDEX], lst[EDGE_LAST_INDEX])

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_edge_elements(sample_data)
    print(result)