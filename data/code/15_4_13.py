def get_penultimate(lst):
    if len(lst) < 2:
        return None
    return lst[-2]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = []
    sample_list_3 = [15]
    sample_list_4 = ['a', 'b', 'c']
    print(get_penultimate(sample_list_1))
    print(get_penultimate(sample_list_2))
    print(get_penultimate(sample_list_3))
    print(get_penultimate(sample_list_4))