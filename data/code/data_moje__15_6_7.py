def get_penultimate(lst):
    if len(lst) < 2:
        raise ValueError("List must have at least two elements")
    return lst[len(lst) - 2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_penultimate(sample_list))