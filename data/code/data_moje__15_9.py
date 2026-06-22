def get_penultimate(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) < 2:
        raise ValueError("List must have at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_penultimate(sample_list)
    print(result)