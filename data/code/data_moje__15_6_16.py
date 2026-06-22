def get_penultimate(lst):
    if len(lst) < 2:
        return None
    return lst[len(lst) - 2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_penultimate(sample_list)
    print(result)