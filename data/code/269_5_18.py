import re

def find_unique_punctuation(text):
    punctuation = set(re.findall(r'[^\w\s]', text))
    return list(punctuation)

if __name__ == '__main__':
    sample_text = "Hello, world! How's it going? Let's meet at 3:00 PM."
    unique_punctuation = find_unique_punctuation(sample_text)
    print(unique_punctuation)