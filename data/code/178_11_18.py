import re

def extract_alphanumeric_words(phrase):
    if not isinstance(phrase, str) or not phrase:
        raise ValueError('Input must be a non-empty string')
    words = re.findall('\\b\\w+\\b', phrase)
    return words
if __name__ == '__main__':
    test_phrase1 = 'Hello world, this is a test phrase 123.'
    result1 = extract_alphanumeric_words(test_phrase1)
    print(f"Phrase: '{test_phrase1}'")
    print(f'Extracted words: {result1}')
    test_phrase2 = 'AlphaBetaGamma 456XYZ and some punctuation!'
    result2 = extract_alphanumeric_words(test_phrase2)
    print(f"Phrase: '{test_phrase2}'")
    print(f'Extracted words: {result2}')
    test_phrase3 = 'NoWordsHere12345'
    result3 = extract_alphanumeric_words(test_phrase3)
    print(f"Phrase: '{test_phrase3}'")
    print(f'Extracted words: {result3}')