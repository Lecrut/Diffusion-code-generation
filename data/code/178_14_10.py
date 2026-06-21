import re

def split_phrase(phrase):
    return [word.strip() for word in re.split(r'\s+', phrase) if word]

if __name__ == '__main__':
    sample_phrase = "Hello,   world! This is a test."
    print(split_phrase(sample_phrase))