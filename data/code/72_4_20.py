def extract_pair_at_index(list_a, list_b, index):
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    if index < 0 or index >= len(list_a) or index >= len(list_b):
        raise ValueError("Index out of range for one or both lists")
    
    lookup_table = {
        "first": list_a[index],
        "second": list_b[index]
    }
    
    return [(lookup_table["first"], lookup_table["second"])]

if __name__ == '__main__':
    source_list_one = [100, 200, 300]
    source_list_two = [400, 500, 600]
    target_index = 2
    combined_result = extract_pair_at_index(source_list_one, source_list_two, target_index)
    print(combined_result)