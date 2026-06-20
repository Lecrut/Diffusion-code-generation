def negate_boolean(value: bool) -> bool:
    return not value

if __name__ == '__main__':
    is_active = False
    negated_value = negate_boolean(is_active)
    print(f"Negation of {is_active}: {negated_value}")