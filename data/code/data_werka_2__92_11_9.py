def negate_boolean_string(text: str) -> str:
    normalized = text.strip().lower()
    if normalized in ('true', 't', '1', 'yes', 'y'):
        return 'False'
    if normalized in ('false', 'f', '0', 'no', 'n'):
        return 'True'
    raise ValueError(f"Invalid boolean string: {text}")

if __name__ == '__main__':
    print(negate_boolean_string('True'))
    print(negate_boolean_string('FALSE'))
    print(negate_boolean_string('yes'))
    print(negate_boolean_string('0'))
    print(negate_boolean_string(' 1 '))
    print(negate_boolean_string('no'))