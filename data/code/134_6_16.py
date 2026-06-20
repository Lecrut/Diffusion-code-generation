def is_mutually_exclusive_set(s):
    count = 0
    for value in s:
        if value:
            count += 1
            if count > 1:
                return False
    return count == 1
if __name__ == '__main__':
    sample_set = {False, True}
    print(is_mutually_exclusive_set(sample_set))
    sample_set2 = {True, True}
    print(is_mutually_exclusive_set(sample_set2))