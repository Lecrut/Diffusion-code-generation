def build_string_from_parts(parts):
    return ' '.join(parts)

if __name__ == '__main__':
    sample_parts = ["Hello", "world", "from", "Alibaba", "Cloud"]
    result = build_string_from_parts(sample_parts)
    print(result)