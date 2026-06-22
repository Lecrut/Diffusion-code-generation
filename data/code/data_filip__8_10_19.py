def split_string(s):
    if not s:
        return []
    parts = s.split(',')
    result = [part.strip() for part in parts if part.strip()]
    return result

if __name__ == '__main__':
    sample_input = "  hello ,  world , , foo , bar  "
    output = split_string(sample_input)
    print(output)