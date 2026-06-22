def get_third_element(lst):
    if len(lst) < 3:
        raise IndexError("List must have at least three elements")
    return lst[2]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    result = get_third_element(sample_list)
    print(result)