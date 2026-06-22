import string

def has_special_chars(text):
    return any(char not in string.ascii_letters + string.digits + ' ' for char in text)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Hello@World!"
    print(has_special_chars(sample1))
    print(has_special_chars(sample2))