def convert_cases(text):
    return text.lower(), text.upper(), text.title()

if __name__ == '__main__':
    sample_text = "Hello, World!"
    lower, upper, title = convert_cases(sample_text)
    print(lower)
    print(upper)
    print(title)