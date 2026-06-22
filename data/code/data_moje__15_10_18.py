def get_penultimate_element(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_penultimate_element(sample_list)
    print(result)