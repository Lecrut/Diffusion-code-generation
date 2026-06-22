def capitalize_first_chars(strings):
    return [s[:1].upper() + s[1:] if s else s for s in strings]

if __name__ == '__main__':
    sample_list = ["hello", "world", "", "python", "test"]
    result = capitalize_first_chars(sample_list)
    print(result)