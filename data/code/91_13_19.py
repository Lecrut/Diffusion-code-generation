def negate_boolean(b):
    return b ^ True
if __name__ == '__main__':
    sample1 = False
    sample2 = True
    print(negate_boolean(sample1))
    print(negate_boolean(sample2))