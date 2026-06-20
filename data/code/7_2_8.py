import string

def contains_special_characters(input_string):
    special_characters = set("!@#$%^&*()-_=+[]{}|;:',.<>?/`~\"\\")
    string_chars = set(input_string)
    return bool(string_chars.intersection(special_characters))

if __name__ == '__main__':
    sample_string = "Hello World! 123"
    result = contains_special_characters(sample_string)
    print(result)