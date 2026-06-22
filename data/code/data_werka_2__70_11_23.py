FIRST_INDEX_OFFSET = 0
LAST_INDEX_OFFSET = -1

def get_edge_elements(lst):
    if len(lst) == 0:
        raise ValueError("Input must be non-empty")
    return (lst[FIRST_INDEX_OFFSET], lst[LAST_INDEX_OFFSET])

if __name__ == '__main__':
    sample_data = [7, 14, 21, 28, 35]
    result = get_edge_elements(sample_data)
    print(result)