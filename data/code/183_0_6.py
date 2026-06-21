def validate_names_str(names_str):
    if not isinstance(names_str, str) or not names_str.strip():
        raise ValueError("Input must be a non-empty string containing comma-separated names.")

def strip_names(names_str):
    validate_names_str(names_str)
    return [name.strip() for name in names_str.split(',')]

if __name__ == '__main__':
    sample_names = "  Alice, Bob , Charlie "
    print(strip_names(sample_names))