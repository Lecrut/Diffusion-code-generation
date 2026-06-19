import re

def extract_words(input_string):
    word_pattern = '\\b\\w+\\b'
    words = re.findall(word_pattern, input_string)
    return words
if __name__ == '__main__':
    sample_input = 'Python is an interpreted high-level general-purpose programming language.\n    Its design philosophy emphasizes code readability with its notable use of significant whitespace.'
    extracted_words = extract_words(sample_input)
    print(extracted_words)