def capitalize_first(s):
    return s[0].upper() + s[1:] if s else ''

if __name__ == '__main__':
    sample_values = ["hello", "world", "", "Python", "a"]
    results = [capitalize_first(value) for value in sample_values]
    print(results)