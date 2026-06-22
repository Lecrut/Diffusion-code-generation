import re

def find_first_letter(text):
    match = re.search('[a-zA-Z]', text)
    return match.group(0) if match else None
if __name__ == '__main__':
    sample_text1 = 'Hello, World!'
    sample_text2 = '12345'
    sample_text3 = ''
    print(find_first_letter(sample_text1))
    print(find_first_letter(sample_text2))
    print(find_first_letter(sample_text3))