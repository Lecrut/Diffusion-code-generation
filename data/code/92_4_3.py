def invert_boolean_string(value: str) -> str:
    if value == 'True':
        return 'False'
    elif value == 'False':
        return 'True'
    else:
        raise ValueError(f"Unsupported boolean string: {value}")

if __name__ == '__main__':
    print(invert_boolean_string('True'))
    print(invert_boolean_string('False'))