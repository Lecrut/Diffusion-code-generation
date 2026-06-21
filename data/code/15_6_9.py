def penultimate_element(lst):
    return lst[len(lst) - 2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = penultimate_element(sample_list)
    print(result)