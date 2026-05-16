import string
def format_string(text):
    lowercase_text = text.lower()
    uppercase_text = text.upper()
    titlecase_text = text.title()
    return lowercase_text, uppercase_text, titlecase_text
if __name__ == '__main__':
    sample_string = "Hello World, This is a Test String."
    lower, upper, title = format_string(sample_string)
    print(f"Original: {sample_string}")
    print(f"Lowercase: {lower}")
    print(f"Uppercase: {upper}")
    print(f"Title Case: {title}")