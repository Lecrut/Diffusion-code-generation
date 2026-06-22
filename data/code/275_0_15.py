UPPERCASE_FUNCTION = str.upper

def print_uppercase_strings(string_list):
    for s in string_list:
        print(UPPERCASE_FUNCTION(s))

if __name__ == '__main__':
    sample_list = ["hello", "world", "python", "script"]
    print_uppercase_strings(sample_list)