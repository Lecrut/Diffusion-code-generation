def check_any_true(iterable):
    return any(iterable)

if __name__ == '__main__':
    sample1 = [False, False, True]
    sample2 = (False, False, False)
    print(f"sample1: {check_any_true(sample1)}")
    print(f"sample2: {check_any_true(sample2)}")