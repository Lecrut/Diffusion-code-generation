import re

def replace_spaces_with_underscores(text):
    return re.sub(r' ', '_', text)

if __name__ == '__main__':
    sample_string = "Hello World Example String"
    result = replace_spaces_with_underscores(sample_string)
    print(result)