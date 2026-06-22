def has_special_characters(s):
    return any(not c.isalnum() and not c.isspace() for c in s)

if __name__ == '__main__':
    test_strings = ['HelloWorld', 'User@Name', 'Test123', 'NoSpecial', 'Special#Char!']
    for string in test_strings:
        print(f"{string}: {has_special_characters(string)}")