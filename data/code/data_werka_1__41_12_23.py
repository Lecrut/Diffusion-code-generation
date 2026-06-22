def to_lowercase(s):
    return s.lower()

def to_uppercase(s):
    return s.upper()

def to_title_case(s):
    return s.title()
if __name__ == '__main__':
    sample_string = 'Hello, World!'
    print(to_lowercase(sample_string))
    print(to_uppercase(sample_string))
    print(to_title_case(sample_string))