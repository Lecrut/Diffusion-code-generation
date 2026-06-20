def capitalize_first_char(strings):
    return [s[:1].upper() + s[1:] if s else s for s in strings]

if __name__ == '__main__':
    sample_data = ["hello", "world", "", "python"]
    result = capitalize_first_char(sample_data)
    print(result)