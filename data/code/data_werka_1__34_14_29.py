def capitalize_first(s):
    return s[:1].upper() + s[1:] if s else s

if __name__ == '__main__':
    sample_values = ["hello", "WORLD", "", "Python", "123abc"]
    for value in sample_values:
        print(capitalize_first(value))