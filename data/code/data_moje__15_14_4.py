def get_second_to_last(lst):
    if len(lst) < 2:
        raise ValueError("List must have at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_second_to_last(sample_list)
    print(result)

    another_list = ['a', 'b', 'c']
    result2 = get_second_to_last(another_list)
    print(result2)

    small_list = [10, 20]
    result3 = get_second_to_last(small_list)
    print(result3)