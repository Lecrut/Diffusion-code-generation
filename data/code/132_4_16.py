def negate_if_false(value):
    return not value

if __name__ == '__main__':
    sample1 = True
    sample2 = False
    print(f"sample1: {negate_if_false(sample1)}")
    print(f"sample2: {negate_if_false(sample2)}")