def build_string_from_parts(parts):
    return ' '.join(parts)

if __name__ == '__main__':
    sample_parts_1 = ["hello", "world", "from", "python"]
    output_1 = build_string_from_parts(sample_parts_1)
    print(output_1)

    sample_parts_2 = ["single"]
    output_2 = build_string_from_parts(sample_parts_2)
    print(output_2)

    sample_parts_3 = ["one", "two", "three", "four", "five"]
    output_3 = build_string_from_parts(sample_parts_3)
    print(output_3)