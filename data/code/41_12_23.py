def to_lowercase(text):
    return text.lower()

def to_uppercase(text):
    return text.upper()

def to_title_case(text):
    return text.title()

if __name__ == '__main__':
    sample_text = "PyThOn CoDe StYlE"
    print(to_lowercase(sample_text))
    print(to_uppercase(sample_text))
    print(to_title_case(sample_text))