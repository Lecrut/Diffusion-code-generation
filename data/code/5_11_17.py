def capitalize_first_letter(strings):
    return tuple(s.capitalize() for s in strings)

if __name__ == '__main__':
    sample = ("hello", "WORLD", "PyThOn", "tEsTiNg")
    result = capitalize_first_letter(sample)
    print(result)