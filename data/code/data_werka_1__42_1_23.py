def build_string_from_parts(parts):
    if not parts:
        return ""
    return ' '.join(parts)

if __name__ == '__main__':
    sample_parts = ["hello", "world", "from", "python"]
    output = build_string_from_parts(sample_parts)
    print(output)