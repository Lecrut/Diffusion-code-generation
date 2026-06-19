def validate_string(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

def to_lowercase(s):
    validate_string(s)
    return s.lower()

def to_uppercase(s):
    validate_string(s)
    return s.upper()

def to_title_case(s):
    validate_string(s)
    return s.title()

if __name__ == '__main__':
    sample_text = "Python String Manipulation"
    lowercase_result = to_lowercase(sample_text)
    uppercase_result = to_uppercase(sample_text)
    titlecase_result = to_title_case(sample_text)
    
    print("Original Text:", sample_text)
    print("Lowercase:", lowercase_result)
    print("Uppercase:", uppercase_result)
    print("Title Case:", titlecase_result)