def build_string(parts, separator=""):
    return separator.join(parts)

if __name__ == '__main__':
    sample_parts = ["Hello", "world", "this", "is", "a", "test"]
    separators = {
        "none": "",
        "space": " ",
        "comma": ",",
        "semicolon": ";"
    }
    
    for sep_name, sep_value in separators.items():
        result = build_string(sample_parts, separator=sep_value)
        print(f"Using '{sep_name}' separator: {result}")