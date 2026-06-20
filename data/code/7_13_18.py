import string

def has_non_alphanumeric_non_space_char(text: str) -> bool:
    for char in text:
        if char not in string.ascii_letters and char not in string.digits and char != ' ':
            return True
    return False

if __name__ == '__main__':
    sample_text_1 = "Hello World! 123"
    sample_text_2 = "HelloWorld123"
    
    print(has_non_alphanumeric_non_space_char(sample_text_1))
    print(has_non_alphanumeric_non_space_char(sample_text_2))