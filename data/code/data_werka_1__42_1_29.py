def validate_parts(parts):
    if not isinstance(parts, list):
        raise ValueError("Input must be a list.")
    for part in parts:
        if not isinstance(part, str):
            raise ValueError("All elements in the list must be strings.")

def build_string_from_parts(parts):
    validate_parts(parts)
    return ' '.join(parts)

if __name__ == '__main__':
    sample_parts = ["hello", "world", "from", "python"]
    output = build_string_from_parts(sample_parts)
    print(output)