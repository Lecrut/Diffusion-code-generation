def negate_if_false(boolean_value):
    return not boolean_value

if __name__ == '__main__':
    sample_values = [False, True]
    for value in sample_values:
        print(f"negate_if_false({value}): {negate_if_false(value)}")