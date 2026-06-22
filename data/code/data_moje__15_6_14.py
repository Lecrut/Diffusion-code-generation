def penultimate_element(lst):
    if len(lst) < 2:
        raise ValueError("List must have at least two elements")
    return lst[len(lst) - 2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(penultimate_element(sample_list))