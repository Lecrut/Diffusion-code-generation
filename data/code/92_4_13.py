BOOLEAN_MAP = {'True': 'False', 'False': 'True'}

def toggle_boolean_string(input_str):
    if input_str in BOOLEAN_MAP:
        return BOOLEAN_MAP[input_str]
    raise ValueError(f"Unsupported boolean string: {input_str}")

if __name__ == '__main__':
    print(toggle_boolean_string('True'))
    print(toggle_boolean_string('False'))