def build_string_from_parts(parts):
    if not parts:
        return ""
    result = parts[0]
    for part in parts[1:]:
        result += " " + part
    return result

if __name__ == '__main__':
    sample_parts_1 = ["hello", "world", "from", "python"]
    output_1 = build_string_from_parts(sample_parts_1)
    print(f"Input: {sample_parts_1}")
    print(f"Output: {output_1}")

    sample_parts_2 = ["join", "these", "words"]
    output_2 = build_string_from_parts(sample_parts_2)
    print(f"Input: {sample_parts_2}")
    print(f"Output: {output_2}")

    sample_parts_3 = ["singleword"]
    output_3 = build_string_from_parts(sample_parts_3)
    print(f"Input: {sample_parts_3}")
    print(f"Output: {output_3}")