import string

def is_word_in_text(text, word):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    return word.lower() in words

if __name__ == '__main__':
    text1 = "This is a sample text."
    word1 = "sample"
    result1 = is_word_in_text(text1, word1)
    print(f"'{word1}' in '{text1}': {result1}")

    text2 = "Hello world!"
    word2 = "python"
    result2 = is_word_in_text(text2, word2)
    print(f"'{word2}' in '{text2}': {result2}")

    text3 = "programming is fun."
    word3 = "fun"
    result3 = is_word_in_text(text3, word3)
    print(f"'{word3}' in '{text3}': {result3}")