import string

def has_special_chars(text):
    printable = string.printable
    for char in text:
        if char not in printable:
            return True
    return False

if __name__ == '__main__':
    sample_input_1 = "Hello World"
    sample_input_2 = "Error@404"
    sample_input_3 = "Valid#Text!"
    print(has_special_chars(sample_input_1))
    print(has_special_chars(sample_input_2))
    print(has_special_chars(sample_input_3))