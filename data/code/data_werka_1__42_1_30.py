def build_string_from_parts(parts):
    return ' '.join(parts)

if __name__ == '__main__':
    sample_parts_1 = ["hello", "world", "from", "Qwen"]
    output_1 = build_string_from_parts(sample_parts_1)
    print(f"Input: {sample_parts_1}")
    print(f"Output: {output_1}")

    sample_parts_2 = ["building", "strings", "efficiently"]
    output_2 = build_string_from_parts(sample_parts_2)
    print(f"Input: {sample_parts_2}")
    print(f"Output: {output_2}")

    sample_parts_3 = ["singleword"]
    output_3 = build_string_from_parts(sample_parts_3)
    print(f"Input: {sample_parts_3}")
    print(f"Output: {output_3}")