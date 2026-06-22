def opposite_bool_string(value: str) -> str:
    if value == 'True':
        return 'False'
    elif value == 'False':
        return 'True'
    else:
        raise ValueError(f"Unsupported boolean string: {value}")

if __name__ == '__main__':
    print(opposite_bool_string('True'))
    print(opposite_bool_string('False'))