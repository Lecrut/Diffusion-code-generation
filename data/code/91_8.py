def negate_single_boolean(bool_list):
    if len(bool_list) == 1:
        return not bool_list[0]
    else:
        raise ValueError("Input list must contain exactly one element")
if __name__ == '__main__':
    sample_list_true = [True]
    result_true = negate_single_boolean(sample_list_true)
    print(f"Negation of {sample_list_true}: {result_true}")
    sample_list_false = [False]
    result_false = negate_single_boolean(sample_list_false)
    print(f"Negation of {sample_list_false}: {result_false}")