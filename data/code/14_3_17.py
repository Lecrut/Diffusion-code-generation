def get_third(iterable):
    return next((item for i, item in enumerate(iterable) if i == 2))

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_third(sample_list)
    print(result)