def build_string_from_parts(parts):
    return ' '.join(parts)

if __name__ == '__main__':
    sample_parts = ["hello", "world", "from", "optimized", "python"]
    output = build_string_from_parts(sample_parts)
    print(output)