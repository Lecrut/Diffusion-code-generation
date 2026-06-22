def compress_string(s):
    def validate_input(value):
        return isinstance(value, str)

    if not validate_input(s):
        raise TypeError("Input must be a string")

    if len(s) == 0:
        return ""

    parts = []
    group_char = s[0]
    group_len = 1

    for char in s[1:]:
        if char == group_char:
            group_len += 1
        else:
            parts.append(group_char)
            parts.append(str(group_len))
            group_char = char
            group_len = 1

    parts.append(group_char)
    parts.append(str(group_len))

    return "".join(parts)

if __name__ == '__main__':
    sample_value = 'aabbcc'
    result = compress_string(sample_value)
    print(result)