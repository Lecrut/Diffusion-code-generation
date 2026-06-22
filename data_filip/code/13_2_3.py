def to_camel_case(s):
    if not s:
        return s
    if s == '_':
        return ''
    if not any(c != '_' for c in s):
        return ''
    parts = s.split('_')
    result = ''
    leading_underscores = 0
    for char in s:
        if char == '_':
            leading_underscores += 1
        else:
            break
    trailing_underscores = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '_':
            trailing_underscores += 1
        else:
            break
    clean_parts = [p for p in parts if p]
    if not clean_parts:
        return s
    first_part = clean_parts[0].lower()
    result += first_part
    for part in clean_parts[1:]:
        if part:
            result += part[0].upper()
            if len(part) > 1:
                result += part[1:].lower()
    return result

if __name__ == '__main__':
    samples = [
        'snake_case_example',
        '__leading_underscores',
        'trailing_underscores__',
        '__multiple__underscores__here__',
        'single',
        'a_b_c',
        '___',
        '',
        'alreadyCamelCase',
        'mixed___Multiple___Underscores___Here'
    ]
    for sample in samples:
        print(f"{sample!r} -> {to_camel_case(sample)!r}")