def get_penultimate_element(lst):
    if not lst:
        raise ValueError("List must contain at least two elements")
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_penultimate_element(sample_list)
    print(result)
    
    sample_list_empty = []
    try:
        get_penultimate_element(sample_list_empty)
    except ValueError as e:
        print(f"ValueError raised as expected: {e}")