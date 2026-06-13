import re
def find_all_words(text):
    words = set()
    for word in re.findall(r'\b\w+\b', text.lower()):
        words.add(word)
    return list(words)
if __name__ == '__main__':
    sample_string = "Hello world! This is a test, a test again. Python is fun."
    result = find_all_words(sample_string)
    print(result)