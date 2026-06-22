def compare_first_two_elements(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements.")
    return lst[0] > lst[1]

if __name__ == '__main__':
    sample_list = [5, 3]
    result = compare_first_two_elements(sample_list)
    print(result)