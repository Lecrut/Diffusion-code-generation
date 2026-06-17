import re
def extract_initial_chars(text):
    matches = [word[0] for word in re.findall(r'\w+', text)]
    return ''.join(matches)
if __name__ == '__main__':
    sample_string = "Hello world! This is a test string."
    result = extract_initial_chars(sample_string)
    print(result)