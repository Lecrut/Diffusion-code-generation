def negate_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    sample_values = {True: "True", False: "False"}
    for value, label in sample_values.items():
        negated_value = negate_boolean(value)
        print(f"Negated {label}: {negated_value}")