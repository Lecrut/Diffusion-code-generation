import re

def split_phrase(phrase):
    words = re.split(r'\s+', phrase.strip())
    return [word.rstrip('.,!?') for word in words if word]

if __name__ == '__main__':
    sample_phrase = "Hello,   world! This is a test."
    print(split_phrase(sample_phrase))