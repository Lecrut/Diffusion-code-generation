def build_string_from_parts(parts):
    result = ""
    for i, part in enumerate(parts):
        result += part
        if i < len(parts) - 1:
            result += " "
    return result
if __name__ == '__main__':
    sample_parts = ["hello", "world", "python", "programming"]
    output = build_string_from_parts(sample_parts)
    print(output)