import re
def split_string_efficiently(text):
    return text.split()
if __name__ == '__main__':
    input_string = "  This   is a test string with multiple spaces "
    result = split_string_efficiently(input_string)
    print(result)