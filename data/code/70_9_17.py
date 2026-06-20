def check_endpoints(iterable):
    return next(iter(iterable)), iterable[-1] if iterable else None

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(check_endpoints(sample_list))
    empty_list = []
    print(check_endpoints(empty_list))