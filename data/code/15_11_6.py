def get_penultimate_value(lst):
    if not isinstance(lst, list) or len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_penultimate_value(sample_list)
    print(result)