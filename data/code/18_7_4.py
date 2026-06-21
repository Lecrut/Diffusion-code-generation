def get_middle(lst):
    length = len(lst)
    index = length // 2
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle(sample_list)
    print(result)