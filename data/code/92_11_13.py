def opposite_boolean_string(value: str) -> str:
    lower_val = value.strip().lower()
    if lower_val == 'true':
        return 'False'
    if lower_val == 'false':
        return 'True'
    raise ValueError(f"Unsupported boolean string: {value}")

if __name__ == '__main__':
    print(opposite_boolean_string('True'))
    print(opposite_boolean_string('false'))
    print(opposite_boolean_string('TRUE'))
    print(opposite_boolean_string('FALSE'))