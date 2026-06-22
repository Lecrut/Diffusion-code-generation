DELIMITERS = " ,.!?"

def clean_word(word):
    return ''.join(char for char in word if char not in DELIMITERS)

def find_words(text):
    words = text.split()
    cleaned_words = [clean_word(word) for word in words]
    return [word for word in cleaned_words if word]

if __name__ == '__main__':
    sample_text = "Hello world this is a test. Python programming is fun and educational!"
    print(find_words(sample_text))