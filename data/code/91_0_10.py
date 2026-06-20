def negate_boolean(value: bool) -> bool:
    negated_values = {True: False, False: True}
    return negated_values[value]

if __name__ == '__main__':
    sample_value = True
    print(f"Original value: {sample_value}")
    print(f"Negated value: {negate_boolean(sample_value)}")