def to_lowercase(s):
    return s.lower()

def to_uppercase(s):
    return s.upper()

def to_title_case(s):
    return s.title()

if __name__ == '__main__':
    sample_values = {
        'original': "Hello, World!",
        'mixed_case': "Python STRING manipULATION",
        'all_lowercase': "already lowercase",
        'all_uppercase': "ALREADY UPPERCASE"
    }
    
    for key, value in sample_values.items():
        print(f"Original {key}: {value}")
        print(f"Lowercase: {to_lowercase(value)}")
        print(f"Uppercase: {to_uppercase(value)}")
        print(f"Title Case: {to_title_case(value)}\n")