def negate_single_boolean(data):
    if not data:
        return None
    return not data[0]
if __name__ == '__main__':
    sample_list = [True]
    result = negate_single_boolean(sample_list)
    print(result)
    sample_list_false = [False]
    result_false = negate_single_boolean(sample_list_false)
    print(result_false)