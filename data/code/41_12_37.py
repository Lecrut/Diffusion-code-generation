def to_lowercase(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s.lower()

def to_uppercase(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s.upper()

def to_title_case(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s.title()

if __name__ == '__main__':
    sample_string = "Hello, World!"
    try:
        print(to_lowercase(sample_string))
        print(to_uppercase(sample_string))
        print(to_title_case(sample_string))
    except ValueError as e:
        print(e)