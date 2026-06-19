def build_string_from_parts(parts, separator=None):
    if not parts:
        return ""
    if separator is None:
        return "".join(parts)
    return separator.join(parts)

if __name__ == '__main__':
    sample_parts1 = ["apple", "banana", "cherry"]
    sample_separator1 = ","
    result1 = build_string_from_parts(sample_parts1, sample_separator1)
    print(f"Parts: {sample_parts1}, Separator: '{sample_separator1}' -> Result: '{result1}'")

    sample_parts2 = ["hello", "world"]
    sample_separator2 = " "
    result2 = build_string_from_parts(sample_parts2, sample_separator2)
    print(f"Parts: {sample_parts2}, Separator: '{sample_separator2}' -> Result: '{result2}'")

    sample_parts3 = ["one", "two", "three"]
    sample_separator3 = ""
    result3 = build_string_from_parts(sample_parts3, sample_separator3)
    print(f"Parts: {sample_parts3}, Separator: '{sample_separator3}' -> Result: '{result3}'")

    sample_parts4 = []
    sample_separator4 = ","
    result4 = build_string_from_parts(sample_parts4, sample_separator4)
    print(f"Parts: {sample_parts4}, Separator: '{sample_separator4}' -> Result: '{result4}'")