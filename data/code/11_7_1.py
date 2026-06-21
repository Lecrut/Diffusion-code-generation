def get_last_element(lst):
    reversed_iter = reversed(lst)
    return next(reversed_iter)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_element(sample_list)
    print(result)