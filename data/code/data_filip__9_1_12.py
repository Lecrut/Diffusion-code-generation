def clean_strings(strings):
    cleaned = []
    for s in strings:
        cleaned.append(s.strip())
    return cleaned

if __name__ == '__main__':
    sample_data = ["  hello  ", " world ", "  python ", "test  "]
    result = clean_strings(sample_data)
    print(result)