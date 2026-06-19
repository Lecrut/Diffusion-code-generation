def case_converter(s):
    lower = ""
    upper = ""
    title = ""
    
    for char in s:
        if 'a' <= char <= 'z':
            lower += char
            upper += chr(ord(char) - 32)
            title += chr(ord(char) - 32) if not title else char
        elif 'A' <= char <= 'Z':
            lower += chr(ord(char) + 32)
            upper += char
            title += char if not title else chr(ord(char) + 32)
        else:
            lower += char
            upper += char
            title += char
    
    return lower, upper, title

if __name__ == '__main__':
    sample_string = "Hello World!"
    lowercase, uppercase, titlecase = case_converter(sample_string)
    print(lowercase)
    print(uppercase)
    print(titlecase)