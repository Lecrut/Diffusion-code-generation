def get_central_element(lst):
    if not lst:
        return None
    index = len(lst) // 2
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_central_element(sample_list)
    print(result)