def capitalize_first(tuples_of_strings):
    return tuple(s.capitalize() if isinstance(s, str) else s for s in tuples_of_strings)

if __name__ == '__main__':
    sample = ("hELLO", "WORLD", "PyThOn", "tESTiNg")
    print(capitalize_first(sample))