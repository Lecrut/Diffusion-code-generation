def capitalize_mixed_case_strings(strings):
    return tuple(s.capitalize() for s in strings)

if __name__ == '__main__':
    sample_data = ("hello", "WORLD", "PyThOn", "tEsT")
    result = capitalize_mixed_case_strings(sample_data)
    print(result)