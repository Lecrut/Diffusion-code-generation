def get_penultimate(lst):
    if len(lst) < 2:
        return None
    return lst[len(lst) - 2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_penultimate(sample_list)
    print(result)