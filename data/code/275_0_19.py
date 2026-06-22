UPPERCASE_CONVERSION = str.upper

def print_uppercase_strings(strings):
    for string in strings:
        print(UPPERCASE_CONVERSION(string))

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "script"]
    print_uppercase_strings(sample_strings)