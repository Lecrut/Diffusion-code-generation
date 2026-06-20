import string

def has_special_characters(text):
    printable_ascii = set(string.printable)
    for char in text:
        if char not in printable_ascii:
            return True
    return False

if __name__ == '__main__':
    sample_1 = "HelloWorld123"
    sample_2 = "Hello@World#123"
    result_1 = has_special_characters(sample_1)
    result_2 = has_special_characters(sample_2)
    print(result_1)
    print(result_2)