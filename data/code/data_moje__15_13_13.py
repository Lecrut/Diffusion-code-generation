def penultimate_element(lst):
    if len(lst) < 2:
        return None
    return lst[-2]

if __name__ == '__main__':
    print(penultimate_element([]))
    print(penultimate_element([1]))
    print(penultimate_element([1, 2]))
    print(penultimate_element([1, 2, 3, 4, 5]))
    print(penultimate_element(['a', 'b', 'c']))
    print(penultimate_element([None, 42]))