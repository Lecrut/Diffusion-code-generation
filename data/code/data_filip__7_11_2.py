def verify_no_special_characters(text):
    return text.isalnum() if text else True

if __name__ == '__main__':
    print(verify_no_special_characters("HelloWorld123"))
    print(verify_no_special_characters("Hello World"))
    print(verify_no_special_characters("Test@123"))
    print(verify_no_special_characters(""))
    print(verify_no_special_characters("12345"))
    print(verify_no_special_characters("abcXYZ"))