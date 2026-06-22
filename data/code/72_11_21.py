def compare_first_and_sixth(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    if len(lst) < 6:
        raise ValueError("List must have at least 6 elements")
    return lst[0] > lst[5]

if __name__ == '__main__':
    sample_data = [10, 2, 3, 4, 5, 1]
    print(compare_first_and_sixth(sample_data))