def get_third(iterable):
    iterator = iter(iterable)
    for _ in range(2):
        next(iterator)
    return next(iterator)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_third(sample_list)
    print(result)