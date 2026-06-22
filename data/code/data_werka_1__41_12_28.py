def to_lowercase(s):
    return s.lower()

def to_uppercase(s):
    return s.upper()

def to_title_case(s):
    return s.title()

if __name__ == '__main__':
    original_text = "Alibaba Cloud"
    lowercased_text = to_lowercase(original_text)
    uppercased_text = to_uppercase(original_text)
    titled_text = to_title_case(original_text)

    print("Original Text:", original_text)
    print("Lowercased Text:", lowercased_text)
    print("Uppercased Text:", uppercased_text)
    print("Titled Text:", titled_text)