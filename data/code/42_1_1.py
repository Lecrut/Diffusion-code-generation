def build_string_from_parts(parts):
    result = ""
    for i, part in enumerate(parts):
        result += part
        if i < len(parts) - 1:
            result += " "
    return result
if __name__ == '__main__':
    sample_parts_1 = ["hello", "world", "python"]
    output_1 = build_string_from_parts(sample_parts_1)
    print(f"Input: {sample_parts_1}")
    print(f"Output: {output_1}")
    sample_parts_2 = ["one", "two", "three", "four"]
    output_2 = build_string_from_parts(sample_parts_2)
    print(f"Input: {sample_parts_2}")
    print(f"Output: {output_2}")
    sample_parts_3 = ["single"]
    output_3 = build_string_from_parts(sample_parts_3)
    print(f"Input: {sample_parts_3}")
    print(f"Output: {output_3}")
    sample_parts_4 = []
    output_4 = build_string_from_parts(sample_parts_4)
    print(f"Input: {sample_parts_4}")
    print(f"Output: {output_4}")