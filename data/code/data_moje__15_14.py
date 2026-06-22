def second_to_last(items):
    if len(items) < 2:
        raise ValueError("List must have at least two elements")
    return items[-2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = second_to_last(sample_list)
    print(result)

    another_list = ['a', 'b', 'c']
    result2 = second_to_last(another_list)
    print(result2)

    single_element_list = [42]
    try:
        second_to_last(single_element_list)
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        second_to_last(empty_list)
    except ValueError as e:
        print(e)