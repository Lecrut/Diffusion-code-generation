import string

def has_special_characters(text):
    allowed = string.ascii_letters + string.digits + string.whitespace
    return any(char not in allowed for char in text)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Hello@World"
    sample3 = "123456"
    sample4 = "Special!Char"
    print(has_special_characters(sample1))
    print(has_special_characters(sample2))
    print(has_special_characters(sample3))
    print(has_special_characters(sample4))