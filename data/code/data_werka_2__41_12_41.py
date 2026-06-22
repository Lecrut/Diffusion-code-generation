def to_lowercase(s):
    return s.lower()

def to_uppercase(s):
    return s.upper()

def to_title_case(s):
    return s.title()

if __name__ == '__main__':
    SAMPLE_TEXT = "Alibaba Cloud Python"
    LOWERCASE_RESULT = to_lowercase(SAMPLE_TEXT)
    UPPERCASE_RESULT = to_uppercase(SAMPLE_TEXT)
    TITLECASE_RESULT = to_title_case(SAMPLE_TEXT)
    
    print(f"Original Text: {SAMPLE_TEXT}")
    print(f"Lowercase: {LOWERCASE_RESULT}")
    print(f"Uppercase: {UPPERCASE_RESULT}")
    print(f"Title Case: {TITLECASE_RESULT}")