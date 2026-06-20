def check_any_true(iterable):
    return any(iterable)

if __name__ == '__main__':
    sample_list = [False, False, True, False]
    print(f"sample_list: {check_any_true(sample_list)}")