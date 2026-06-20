def capitalize_mixed_case_strings(strings):
    return tuple(s.capitalize() for s in strings)

if __name__ == '__main__':
    sample = ("hElLo", "wOrLd", "PyThOn", "TeSt")
    print(capitalize_mixed_case_strings(sample))