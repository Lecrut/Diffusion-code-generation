def determine_both_false(val1, val2):
    return not bool(val1) and not bool(val2)

if __name__ == '__main__':
    sample1 = 0
    sample2 = ''
    result = determine_both_false(sample1, sample2)
    print(result)