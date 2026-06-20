def compare_pairs(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Both inputs must be lists.")
    
    min_length = min(len(list1), len(list2))
    
    for a, b in zip(list1[:min_length], list2[:min_length]):
        if a > b:
            yield f'{a} > {b}'
        elif a < b:
            yield f'{a} < {b}'
        else:
            yield f'{a} == {b}'

if __name__ == '__main__':
    list_a = [3, 5, 7]
    list_b = [2, 4, 6]
    output = compare_pairs(list_a, list_b)
    print(list(output))