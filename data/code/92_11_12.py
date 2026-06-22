def opposite_bool_string(value: str) -> str:
    if value.lower() == 'true':
        return 'False'
    elif value.lower() == 'false':
        return 'True'
    else:
        raise ValueError(f"Unsupported boolean string: {value}")

if __name__ == '__main__':
    print(opposite_bool_string('True'))
    print(opposite_bool_string('False'))
    print(opposite_bool_string('TRUE'))
    print(opposite_bool_string('FALSE'))
    print(opposite_bool_string('true'))
    print(opposite_bool_string('false'))