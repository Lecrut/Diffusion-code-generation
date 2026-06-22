def to_lowercase(input_string):
    return input_string.lower()

def to_uppercase(input_string):
    return input_string.upper()

def to_title_case(input_string):
    return input_string.title()
if __name__ == '__main__':
    sample_string = 'Hello, World!'
    print(to_lowercase(sample_string))
    print(to_uppercase(sample_string))
    print(to_title_case(sample_string))