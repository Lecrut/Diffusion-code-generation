def build_string(parts, joiner):
    if not parts:
        return ""
    if joiner is None:
        return "".join(parts)
    return joiner.join(parts)
if __name__ == '__main__':
    parts1 = ["apple", "banana", "cherry"]
    print(f"Parts: {parts1}, Joiner: None -> Result: {build_string(parts1, None)}")
    parts2 = ["red", "green", "blue"]
    print(f"Parts: {parts2}, Joiner: ' ' -> Result: {build_string(parts2, ' ')}")
    parts3 = ["one", "two", "three"]
    print(f"Parts: {parts3}, Joiner: ', ' -> Result: {build_string(parts3, ', ')}")
    parts4 = ["a", "b", "c"]
    print(f"Parts: {parts4}, Joiner: '' -> Result: {build_string(parts4, '')}")
    parts5 = ["hello", "world"]
    print(f"Parts: {parts5}, Joiner: '-' -> Result: {build_string(parts5, '-')}")
    parts6 = []
    print(f"Parts: {parts6}, Joiner: ',' -> Result: {build_string(parts6, ',')}")