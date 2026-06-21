def opposite_boolean_string(value: str) -> str:
    if value.lower() == 'true':
        return 'False'
    if value.lower() == 'false':
        return 'True'
    raise ValueError(f"Unsupported boolean string: {value}")

if __name__ == '__main__':
    print(opposite_boolean_string('True'))
    print(opposite_boolean_string('False'))
    print(opposite_boolean_string('TRUE'))
    print(opposite_boolean_string('FALSE'))
    print(opposite_boolean_string('true'))
    print(opposite_boolean_string('false'))