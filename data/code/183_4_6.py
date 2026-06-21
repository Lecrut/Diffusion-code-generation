def validate_names_str(names_str):
    if not isinstance(names_str, str) or '\n' not in names_str:
        raise ValueError("Input must be a string containing newline-separated names.")
    return names_str.strip()

def convert_names_to_list(names_str):
    validated_names = validate_names_str(names_str)
    return [name.strip() for name in validated_names.split('\n') if name.strip()]

if __name__ == '__main__':
    sample_names = "Alice\nBob\nCharlie"
    print(convert_names_to_list(sample_names))