def get_last_element(lst):
    iterator = reversed(lst)
    return next(iterator)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_element(sample_list)
    print(result)