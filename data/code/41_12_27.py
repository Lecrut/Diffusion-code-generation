def to_lowercase(s):
    return s.lower()

def to_uppercase(s):
    return s.upper()

def to_title_case(s):
    return s.title()

if __name__ == '__main__':
    SAMPLE_TEXT = "Python String Manipulation"
    LOWERCASE_RESULT = to_lowercase(SAMPLE_TEXT)
    UPPERCASE_RESULT = to_uppercase(SAMPLE_TEXT)
    TITLECASE_RESULT = to_title_case(SAMPLE_TEXT)
    
    print("Original Text:", SAMPLE_TEXT)
    print("Lowercase:", LOWERCASE_RESULT)
    print("Uppercase:", UPPERCASE_RESULT)
    print("Title Case:", TITLECASE_RESULT)