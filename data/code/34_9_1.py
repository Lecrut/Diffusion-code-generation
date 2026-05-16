import re
def capitalize_words(text):
    return text.title()
if __name__ == '__main__':
    sample_string = "this is a sample string for capitalization"
    result = capitalize_words(sample_string)
    print(result)