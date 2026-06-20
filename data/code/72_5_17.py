def compare_pairs(list1, list2):
    if not all(isinstance(item, (int, float)) for item in list1 + list2):
        raise ValueError("Both lists must contain only integers or floats")
    
    length = min(len(list1), len(list2))
    
    for a, b in zip(list1[:length], list2[:length]):
        if a > b:
            yield f'{a} > {b}'
        elif a < b:
            yield f'{a} < {b}'
        else:
            yield f'{a} == {b}'

if __name__ == '__main__':
    try:
        result = compare_pairs([1, 2, 3], [3, 2, 1])
        for comparison in result:
            print(comparison)
    except ValueError as e:
        print(e)