def complement_bool_str(text: str) -> str:
    if not text:
        raise ValueError("Empty string is not a valid boolean representation")
    clean = text.strip().lower()
    if clean in ('true', 't', '1', 'yes', 'y'):
        return 'False'
    if clean in ('false', 'f', '0', 'no', 'n'):
        return 'True'
    raise ValueError(f"Unrecognized boolean string: {text}")

if __name__ == '__main__':
    print(complement_bool_str('True'))
    print(complement_bool_str('false'))
    print(complement_bool_str('TRUE'))
    print(complement_bool_str('FALSE'))
    print(complement_bool_str('yes'))
    print(complement_bool_str('no'))
    print(complement_bool_str('1'))
    print(complement_bool_str('0'))
    print(complement_bool_str(' Y '))
    print(complement_bool_str(' N '))