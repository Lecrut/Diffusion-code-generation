def trim_names(name_string):
    if not isinstance(name_string, str) or '-' not in name_string:
        raise ValueError("Input must be a hyphen-separated string")
    
    return [name.strip() for name in name_string.split('-')]

if __name__ == '__main__':
    sample_input = "  John-Doe - Jane-Smith  "
    print(trim_names(sample_input))