def toggle_boolean_str(s: str) -> str:
    if s == 'True':
        return 'False'
    if s == 'False':
        return 'True'
    raise ValueError("Invalid boolean string")

if __name__ == '__main__':
    print(toggle_boolean_str('True'))
    print(toggle_boolean_str('False'))