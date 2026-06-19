def convert_string(s):
    lowercase = s.lower()
    uppercase = s.upper()
    titlecase = s.title()
    return lowercase, uppercase, titlecase

if __name__ == '__main__':
    sample_string = "Hello World"
    lower, upper, title = convert_string(sample_string)
    print(lower)
    print(upper)
    print(title)