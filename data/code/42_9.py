def build_string(parts, separator):
    if not parts:
        return ""
    if separator is None:
        return "".join(parts)
    return separator.join(parts)
if __name__ == '__main__':
    parts1 = ["apple", "banana", "cherry"]
    sep1 = ","
    result1 = build_string(parts1, sep1)
    print(f"Parts: {parts1}, Separator: '{sep1}' -> Result: '{result1}'")
    parts2 = ["Hello", "world"]
    sep2 = " "
    result2 = build_string(parts2, sep2)
    print(f"Parts: {parts2}, Separator: '{sep2}' -> Result: '{result2}'")
    parts3 = ["one", "two", "three"]
    sep3 = ""
    result3 = build_string(parts3, sep3)
    print(f"Parts: {parts3}, Separator: '{sep3}' -> Result: '{result3}'")
    parts4 = ["a", "b", "c", "d"]
    sep4 = "---"
    result4 = build_string(parts4, sep4)
    print(f"Parts: {parts4}, Separator: '{sep4}' -> Result: '{result4}'")
    parts5 = ["single"]
    sep5 = None
    result5 = build_string(parts5, sep5)
    print(f"Parts: {parts5}, Separator: {sep5} -> Result: '{result5}'")
    parts6 = []
    sep6 = ","
    result6 = build_string(parts6, sep6)
    print(f"Parts: {parts6}, Separator: '{sep6}' -> Result: '{result6}'")