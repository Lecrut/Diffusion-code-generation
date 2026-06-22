def toggle_boolean_string(input_str):
    if input_str == 'True':
        return 'False'
    if input_str == 'False':
        return 'True'
    raise ValueError(f"Invalid boolean string: {input_str}")

if __name__ == '__main__':
    print(toggle_boolean_string('True'))
    print(toggle_boolean_string('False'))