def negate_boolean(value: bool) -> bool:
    negation = {True: False, False: True}
    return negation[value]

if __name__ == '__main__':
    sample_value = True
    result = negate_boolean(sample_value)
    print(f"Original value: {sample_value}")
    print(f"Negated value: {result}")