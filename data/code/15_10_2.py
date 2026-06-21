def get_penultimate_element(lst):
    if len(lst) < 2:
        raise ValueError("List must have at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_penultimate_element(sample_list)
    print(result)
    
    another_list = [10, 20, 30]
    result2 = get_penultimate_element(another_list)
    print(result2)
    
    try:
        get_penultimate_element([])
    except ValueError as e:
        print(e)
    
    try:
        get_penultimate_element([1])
    except ValueError as e:
        print(e)