import re

def isolate_words(phrase):
    words = re.findall(r'\b\w+\b', phrase)
    return [word for word in words if word]

if __name__ == '__main__':
    sample_phrase = "Hello, world! 123 is a number."
    print(isolate_words(sample_phrase))