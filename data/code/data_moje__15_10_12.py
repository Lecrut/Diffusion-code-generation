def get_penultimate_element(lst):
    if len(lst) < 2:
        raise ValueError("List must have at least two elements")
    return lst[-2]

if __name__ == '__main__':
    print(get_penultimate_element([1, 2, 3, 4, 5]))
    print(get_penultimate_element(['a', 'b']))
    try:
        print(get_penultimate_element([]))
    except ValueError as e:
        print(e)
    try:
        print(get_penultimate_element([42]))
    except ValueError as e:
        print(e)