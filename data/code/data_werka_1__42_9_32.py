def build_string_from_parts(parts, separator=None):
    if not parts:
        return ""
    return (separator or "").join(parts)

if __name__ == '__main__':
    PARTS1 = ["apple", "banana", "cherry"]
    SEPARATOR1 = ","
    RESULT1 = build_string_from_parts(PARTS1, SEPARATOR1)
    print(f"Parts: {PARTS1}, Separator: '{SEPARATOR1}' -> Result: '{RESULT1}'")

    PARTS2 = ["Hello", "world"]
    SEPARATOR2 = " "
    RESULT2 = build_string_from_parts(PARTS2, SEPARATOR2)
    print(f"Parts: {PARTS2}, Separator: '{SEPARATOR2}' -> Result: '{RESULT2}'")

    PARTS3 = ["one", "two", "three"]
    SEPARATOR3 = ""
    RESULT3 = build_string_from_parts(PARTS3, SEPARATOR3)
    print(f"Parts: {PARTS3}, Separator: '{SEPARATOR3}' -> Result: '{RESULT3}'")

    PARTS4 = []
    SEPARATOR4 = ","
    RESULT4 = build_string_from_parts(PARTS4, SEPARATOR4)
    print(f"Parts: {PARTS4}, Separator: '{SEPARATOR4}' -> Result: '{RESULT4}'")