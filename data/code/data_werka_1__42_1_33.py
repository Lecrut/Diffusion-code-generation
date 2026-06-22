def build_string_from_parts(parts):
    SEPARATOR = " "
    return SEPARATOR.join(parts)

if __name__ == '__main__':
    SAMPLE_PARTS_1 = ["Hello", "world", "from", "Python"]
    RESULT_1 = build_string_from_parts(SAMPLE_PARTS_1)
    print(f"Input: {SAMPLE_PARTS_1}")
    print(f"Output: {RESULT_1}")

    SAMPLE_PARTS_2 = ["Joining", "strings", "efficiently"]
    RESULT_2 = build_string_from_parts(SAMPLE_PARTS_2)
    print(f"Input: {SAMPLE_PARTS_2}")
    print(f"Output: {RESULT_2}")

    SAMPLE_PARTS_3 = ["SingleElement"]
    RESULT_3 = build_string_from_parts(SAMPLE_PARTS_3)
    print(f"Input: {SAMPLE_PARTS_3}")
    print(f"Output: {RESULT_3}")