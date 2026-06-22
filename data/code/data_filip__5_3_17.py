def capitalize_first_alphanumeric(s):
    result = []
    capitalized = False
    for char in s:
        if not capitalized and char.isalnum():
            result.append(char.upper())
            capitalized = True
        else:
            result.append(char)
        if capitalized and len(result) > 0:
            break
    return ''.join(result) + s[len(result):]

if __name__ == '__main__':
    print(capitalize_first_alphanumeric("hello world"))
    print(capitalize_first_alphanumeric("123abc"))
    print(capitalize_first_alphanumeric("   space first"))
    print(capitalize_first_alphanumeric(""))
    print(capitalize_first_alphanumeric("no alnum here!!!"))