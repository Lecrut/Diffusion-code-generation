def has_no_special_characters(s):
    return s.isalnum() or s == ""

if __name__ == '__main__':
    print(has_no_special_characters("HelloWorld"))
    print(has_no_special_characters("Hello World!"))
    print(has_no_special_characters("12345"))
    print(has_no_special_characters("test@123"))
    print(has_no_special_characters(""))
    print(has_no_special_characters("a b c"))
    print(has_no_special_characters("Special#Char$"))