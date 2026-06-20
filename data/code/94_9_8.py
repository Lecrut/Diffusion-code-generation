def check_at_least_one(iterable):
    return any(iterable)

if __name__ == '__main__':
    sample1 = [False, False, False]
    sample2 = [True, False, False]
    sample3 = []
    print(f"sample1: {check_at_least_one(sample1)}")
    print(f"sample2: {check_at_least_one(sample2)}")
    print(f"sample3: {check_at_least_one(sample3)}")