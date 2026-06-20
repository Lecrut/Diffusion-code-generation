def negate_boolean(boolean: bool) -> bool:
    return not boolean

if __name__ == '__main__':
    sample_value = False
    negated_value = negate_boolean(sample_value)
    print(f"Input: {sample_value}, Output: {negated_value}")