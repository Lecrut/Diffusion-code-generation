import re

def extract_word_punctuation(sentence):
    words_with_punct = []
    for word in sentence.split():
        match = re.search(r'(\w+)([^\w\s])', word)
        if match:
            words_with_punct.append((match.group(1), match.group(2)))
    return words_with_punct

if __name__ == '__main__':
    sample_sentence = "Hello, world! How are you?"
    print(extract_word_punctuation(sample_sentence))