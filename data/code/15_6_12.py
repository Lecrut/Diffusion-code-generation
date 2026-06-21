def penultimate_element(lst):
    n = len(lst)
    if n < 2:
        return None
    idx = n - 2
    return lst[idx]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = penultimate_element(sample_list)
    print(result)