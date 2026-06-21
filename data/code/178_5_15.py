def clean_and_split(text):
    words = text.split()
    cleaned_words = []
    for word in words:
        cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
        if cleaned_word:
            cleaned_words.append(cleaned_word)
    return cleaned_words

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with some symbols @#$ and numbers 123."
    result = clean_and_split(sample_string)
    print(result)