def capitalize_strings(strings):
    return tuple(s.capitalize() for s in strings)

if __name__ == '__main__':
    sample = ("hELLO", "WoRLd", "PyThOn", "teSt")
    print(capitalize_strings(sample))