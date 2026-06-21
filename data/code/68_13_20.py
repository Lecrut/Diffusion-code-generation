def find_distinct_items(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    distinct_items = set_a - set_b
    return list(distinct_items)

if __name__ == '__main__':
    SAMPLE_LIST_A = [10, 20, 30, 40, 50]
    SAMPLE_LIST_B = [30, 40, 50, 60, 70]
    
    result = find_distinct_items(SAMPLE_LIST_A, SAMPLE_LIST_B)
    print(result)