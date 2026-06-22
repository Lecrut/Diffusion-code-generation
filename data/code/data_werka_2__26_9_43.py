def check_first_greater(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list = [5, 3]
    try:
        print(check_first_greater(sample_list))
    except ValueError as e:
        print(e)