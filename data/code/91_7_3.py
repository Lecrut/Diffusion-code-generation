def negate_boolean_list(lst):
    return not lst[0]

if __name__ == '__main__':
    sample_list = [True]
    result = negate_boolean_list(sample_list)
    print(result)