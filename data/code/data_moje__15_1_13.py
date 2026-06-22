def get_penultimate(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_penultimate(sample_list)
    print(result)

    short_list = [10]
    try:
        get_penultimate(short_list)
    except ValueError as e:
        print(str(e))