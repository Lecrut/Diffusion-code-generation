def validate_lists(list_one, list_two):
    if not all(isinstance(item, (list, set)) for item in [list_one, list_two]):
        raise ValueError("Both inputs must be lists or sets.")
    return list_one, list_two

def combine_lists(list_one, list_two):
    list_one, list_two = validate_lists(list_one, list_two)
    combined_set = set(list_one).union(set(list_two))
    return list(combined_set)

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = combine_lists(list_a, list_b)
    print(result)
    
    list_c = ['apple', 'banana', 'cherry']
    list_d = ['banana', 'date', 'elderberry']
    result2 = combine_lists(list_c, list_d)
    print(result2)