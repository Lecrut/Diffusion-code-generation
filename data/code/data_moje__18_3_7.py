def get_central_element(lst):
    return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70]
    result = get_central_element(sample_list)
    print(result)