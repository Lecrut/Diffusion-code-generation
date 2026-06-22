def build_string_from_parts(parts):
    if not isinstance(parts, list) or not all(isinstance(part, str) for part in parts):
        raise ValueError("Input must be a list of strings.")
    
    result = []
    for part in parts:
        result.append(part)
    
    return ' '.join(result)

if __name__ == '__main__':
    sample_parts_1 = ["Hello", "world!", "This", "is", "a", "test."]
    output_1 = build_string_from_parts(sample_parts_1)
    print(f"Input: {sample_parts_1}")
    print(f"Output: {output_1}")

    sample_parts_2 = ["single"]
    output_2 = build_string_from_parts(sample_parts_2)
    print(f"Input: {sample_parts_2}")
    print(f"Output: {output_2}")

    sample_parts_3 = ["Join", "these", "words", "together."]
    output_3 = build_string_from_parts(sample_parts_3)
    print(f"Input: {sample_parts_3}")
    print(f"Output: {output_3}")