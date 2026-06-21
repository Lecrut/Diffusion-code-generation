def invert_boolean_string(value: str) -> str:
    if value.lower() == 'true':
        return 'False'
    if value.lower() == 'false':
        return 'True'
    raise ValueError(f"Unsupported boolean string: {value}")

if __name__ == '__main__':
    print(invert_boolean_string('True'))
    print(invert_boolean_string('false'))
    print(invert_boolean_string('TRUE'))
    print(invert_boolean_string('FALSE'))