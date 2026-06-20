import string

def count_special_chars(text):
    count = 0
    is_special_present = False
    special_chars = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    for char in text:
        if char in special_chars:
            count += 1
            is_special_present = True
    return count, is_special_present

if __name__ == '__main__':
    sample_string = "Hello, World! 123 @#$"
    result = count_special_chars(sample_string)
    print(result)