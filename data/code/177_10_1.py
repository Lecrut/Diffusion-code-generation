import re
def split_string(text):
    return text.split()
if __name__ == '__main__':
    input_string = "This is a sample string with  multiple spaces between words"
    result = split_string(input_string)
    print(result)