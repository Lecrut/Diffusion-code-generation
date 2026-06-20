def negate_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    sample_value = True
    negated_value = negate_boolean(sample_value)
    print(negated_value)