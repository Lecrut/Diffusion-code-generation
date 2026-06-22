def has_no_special_characters(text):
    return text.isalnum() if text else True

if __name__ == '__main__':
    print(has_no_special_characters("hello123"))
    print(has_no_special_characters("hello@world"))
    print(has_no_special_characters(""))
    print(has_no_special_characters("Test123!"))