def negate_boolean(boolean_list):
    return not boolean_list[0]

if __name__ == '__main__':
    sample_value = [False]
    negated_result = negate_boolean(sample_value)
    print(f"Negation of {sample_value}: {negated_result}")