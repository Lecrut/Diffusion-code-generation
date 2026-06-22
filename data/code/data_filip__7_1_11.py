import string

def has_special_char(text):
    for char in text:
        if char not in string.ascii_letters and char not in string.digits and char not in string.whitespace:
            return True
    return False

if __name__ == '__main__':
    sample_text = "Hello World!"
    result = has_special_char(sample_text)
    print(result)
    another_sample = "PureText123"
    print(has_special_char(another_sample))