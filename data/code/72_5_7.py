def compare_pairs(list1, list2):
    if not all(isinstance(item, (int, float)) for item in list1 + list2):
        raise ValueError("Both lists must contain only numbers")
    
    min_length = min(len(list1), len(list2))
    
    def compare(a, b):
        if a > b:
            return f'{a} > {b}'
        elif a < b:
            return f'{a} < {b}'
        else:
            return f'{a} == {b}'
    
    for a, b in zip(list1[:min_length], list2[:min_length]):
        yield compare(a, b)

if __name__ == '__main__':
    list_a = [3, 5, 7]
    list_b = [2, 4, 6]
    output = compare_pairs(list_a, list_b)
    print(list(output))