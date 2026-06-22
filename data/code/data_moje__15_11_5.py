def get_penultimate(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_penultimate(sample_list)
    print(result)

    another_list = [1, 2]
    result2 = get_penultimate(another_list)
    print(result2)

    try:
        short_list = [1]
        get_penultimate(short_list)
    except ValueError as e:
        print(e)

    try:
        empty_list = []
        get_penultimate(empty_list)
    except ValueError as e:
        print(e)