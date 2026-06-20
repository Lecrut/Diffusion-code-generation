def first_special_char(s):
    special_characters = set("!?@#$%^&*()-_=+[]{}|;:'\",.<>/`~")
    for char in s:
        if char in special_characters:
            return char
    return None

if __name__ == '__main__':
    print(first_special_char("hello world!"))
    print(first_special_char("no special chars here"))
    print(first_special_char("@start"))
    print(first_special_char("12345"))
    print(first_special_char("test#123"))