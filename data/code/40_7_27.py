import string

def get_initials(text):
    initials = []
    words = text.split()
    for word in words:
        stripped_word = word.strip(string.punctuation)
        if stripped_word:
            initials.append(stripped_word[0])
    return initials
if __name__ == '__main__':
    sample_text = 'Hello, world! This is a test. Punctuation... should be ignored!'
    result = get_initials(sample_text)
    print(result)