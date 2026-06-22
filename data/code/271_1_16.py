FILTER_CONSTANTS = {
    'ALPHABETIC': r'^[a-zA-Z]+$'
}

def filter_alphabetic_strings(strings):
    import re
    pattern = re.compile(FILTER_CONSTANTS['ALPHABETIC'])
    return [s for s in strings if pattern.match(s)]

if __name__ == '__main__':
    sample_values = ["hello", "world", "123", "test", "!@#"]
    result = filter_alphabetic_strings(sample_values)
    print(result)