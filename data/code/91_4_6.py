def negate_boolean(boolean_value):
    return not boolean_value

if __name__ == '__main__':
    sample_input = True
    negated_result = negate_boolean(sample_input)
    print(f"Input: {sample_input}, Output: {negated_result}")