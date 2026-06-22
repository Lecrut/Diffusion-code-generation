def to_camel_case(text):
    if not text:
        return text
    parts = text.split('_')
    if not parts or not parts[0]:
        return text
    result = []
    result.append(parts[0])
    for part in parts[1:]:
        if not part:
            continue
        first_char = part[0]
        rest = part[1:]
        result.append(first_char.upper() + rest)
    return ''.join(result)

if __name__ == '__main__':
    sample_inputs = ['user_name', 'first_name_last_name', 'snake_case_to_camel_case', 'a', 'a_b_c', 'alreadyCamelCase', 'mixed_case_test']
    for s in sample_inputs:
        print(to_camel_case(s))