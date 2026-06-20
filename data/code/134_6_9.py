def is_mutually_exclusive_set(s):
    return sum(1 for x in s if x) == 1

if __name__ == '__main__':
    sample_set = {True, False}
    print(is_mutually_exclusive_set(sample_set))