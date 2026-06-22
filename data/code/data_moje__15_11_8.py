def get_penultimate_value(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        ['a', 'b', 'c'],
        [10, 20],
        [42]
    ]
    
    for sample in sample_lists[:3]:
        result = get_penultimate_value(sample)
        print(result)
    
    try:
        get_penultimate_value(sample_lists[3])
    except ValueError as e:
        print(str(e))