def capitalize_mixed_case_strings(strings: tuple) -> tuple:
    return tuple(s.capitalize() for s in strings)

if __name__ == '__main__':
    sample = ('hello', 'WORLD', 'PyThOn', 'tEsTiNg', 'AbCdEf')
    print(capitalize_mixed_case_strings(sample))