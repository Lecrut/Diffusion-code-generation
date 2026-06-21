def negate_boolean_list(boolean_list):
    return not boolean_list[0]

if __name__ == '__main__':
    sample_list = [True]
    result = negate_boolean_list(sample_list)
    print(result)