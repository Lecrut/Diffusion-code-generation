import string

def has_non_alphanumeric_non_space(text):
    for char in text:
        if not char.isalnum() and char != ' ':
            return True
    return False

if __name__ == '__main__':
    sample_input = "Hello World!"
    result = has_non_alphanumeric_non_space(sample_input)
    print(result)