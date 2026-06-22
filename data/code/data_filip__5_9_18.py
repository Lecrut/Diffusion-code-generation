def capitalize_first_lower_rest(s):
    if not s:
        return s
    return s[0].upper() + s[1:].lower()

if __name__ == '__main__':
    samples = ["hello", "WORLD", "Python", "a", "", "123abc", "hElLo wOrLd"]
    for sample in samples:
        print(capitalize_first_lower_rest(sample))