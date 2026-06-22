import re

def to_camel_case(text):
    if not text:
        return text
    leading_underscores = len(text) - len(text.lstrip('_'))
    trailing_underscores = len(text) - len(text.rstrip('_'))
    core_text = text[leading_underscores:len(text)-trailing_underscores]
    if not core_text:
        return '_' * leading_underscores + '_' * trailing_underscores
    parts = re.split(r'_+', core_text)
    parts = [part for part in parts if part]
    if not parts:
        return '_' * (leading_underscores + trailing_underscores)
    first_part = parts[0].lower()
    camel_parts = [first_part]
    for part in parts[1:]:
        if part:
            camel_parts.append(part[0].upper() + part[1:].lower())
    result = ''.join(camel_parts)
    if leading_underscores > 0:
        result = '_' * leading_underscores + result
    if trailing_underscores > 0:
        result = result + '_' * trailing_underscores
    return result

if __name__ == '__main__':
    sample_inputs = [
        "hello_world",
        "_leading_under",
        "trailing_under_",
        "__double__leading__trailing__",
        "multiple__consecutive__underscores",
        "UPPER_CASE_MIXED",
        "",
        "___",
        "a_b_c"
    ]
    for sample in sample_inputs:
        print(f"{sample!r} -> {to_camel_case(sample)!r}")