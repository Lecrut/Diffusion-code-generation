CASE_LOWER = 'lower'
CASE_UPPER = 'upper'
CASE_TITLE = 'title'

def to_lowercase(s):
    return s.lower()

def to_uppercase(s):
    return s.upper()

def to_title_case(s):
    return s.title()

if __name__ == '__main__':
    sample_text = "Python String Manipulation"
    print(f"Original Text: {sample_text}")
    print(f"{CASE_LOWER.capitalize()} Case: {to_lowercase(sample_text)}")
    print(f"{CASE_UPPER.capitalize()} Case: {to_uppercase(sample_text)}")
    print(f"{CASE_TITLE.capitalize()} Case: {to_title_case(sample_text)}")