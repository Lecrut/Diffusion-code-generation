def normalize_strings(data):
    return tuple(s.capitalize() for s in data)

if __name__ == '__main__':
    sample_input = ("hElLo", "WORLD", "pyThOn", "tUPLe")
    result = normalize_strings(sample_input)
    print(result)