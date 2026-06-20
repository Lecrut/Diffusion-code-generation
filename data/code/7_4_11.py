import string

def find_first_special(s):
    special_chars = set(string.punctuation)
    for char in s:
        if char in special_chars:
            return char
    return None

if __name__ == '__main__':
    sample_string = "Hello World! Welcome to Python@123"
    result = find_first_special(sample_string)
    print(result)