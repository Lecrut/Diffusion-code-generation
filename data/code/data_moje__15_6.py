def get_penultimate(lst):
    if len(lst) < 2:
        return None
    index = len(lst) - 2
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_penultimate(sample_list)
    print(result)