def to_lowercase(s):
    return s.lower()

def to_uppercase(s):
    return s.upper()

def to_title_case(s):
    return s.title()

if __name__ == '__main__':
    sample_text = "Alibaba Cloud Python"
    print("Original Text:", sample_text)
    print("Lowercase:", to_lowercase(sample_text))
    print("Uppercase:", to_uppercase(sample_text))
    print("Title Case:", to_title_case(sample_text))