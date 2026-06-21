def to_lowercase(s):
    return s.lower()

def to_uppercase(s):
    return s.upper()

def to_title_case(s):
    return s.title()
if __name__ == '__main__':
    sample_string = 'Hello World'
    lowercased = to_lowercase(sample_string)
    uppercased = to_uppercase(sample_string)
    titled = to_title_case(sample_string)
    print(lowercased)
    print(uppercased)
    print(titled)