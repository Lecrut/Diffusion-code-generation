def get_second_to_last(lst):
    if len(lst) < 2:
        raise IndexError("List must contain at least two items")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_second_to_last(sample_list)
    print(result)