def get_second_to_last(lst):
    if len(lst) < 2:
        raise IndexError("List must have at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_second_to_last(sample_list)
    print(result)