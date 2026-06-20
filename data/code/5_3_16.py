def capitalize_first_if_alphanumeric(s):
    if s and s[0].isalnum():
        return s[0].upper() + s[1:]
    return s

if __name__ == '__main__':
    print(capitalize_first_if_alphanumeric('hello'))
    print(capitalize_first_if_alphanumeric('123abc'))
    print(capitalize_first_if_alphanumeric('!hello'))
    print(capitalize_first_if_alphanumeric(''))
    print(capitalize_first_if_alphanumeric('a'))
    print(capitalize_first_if_alphanumeric('already Capitalized'))