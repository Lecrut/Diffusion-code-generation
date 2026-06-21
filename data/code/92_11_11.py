def opposite_boolean_string(value: str) -> str:
    def is_truthy(val: str) -> bool:
        return val.strip().lower() in ('true', 't', '1', 'yes', 'y')

    def is_falsy(val: str) -> bool:
        return val.strip().lower() in ('false', 'f', '0', 'no', 'n')

    if is_truthy(value):
        return 'False'
    if is_falsy(value):
        return 'True'
    raise ValueError(f"Invalid boolean string: {value}")

if __name__ == '__main__':
    print(opposite_boolean_string('True'))
    print(opposite_boolean_string('False'))
    print(opposite_boolean_string('YES'))
    print(opposite_boolean_string('0'))
    print(opposite_boolean_string('TRUE'))
    print(opposite_boolean_string('FALSE'))
    print(opposite_boolean_string('1'))
    print(opposite_boolean_string('0'))
    print(opposite_boolean_string('Yes'))
    print(opposite_boolean_string('No'))