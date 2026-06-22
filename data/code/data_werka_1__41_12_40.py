def to_lowercase(s):
    return s.lower()

def to_uppercase(s):
    return s.upper()

def to_title_case(s):
    return s.title()

if __name__ == '__main__':
    sample_string = "Hello, World!"
    print("Original String:", sample_string)
    print("Lowercase:", to_lowercase(sample_string))
    print("Uppercase:", to_uppercase(sample_string))
    print("Title Case:", to_title_case(sample_string))