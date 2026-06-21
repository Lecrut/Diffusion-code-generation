TARGET_WORD = "python"

def text_to_word_set(text):
    return set(word.lower() for word in text.split())

def word_present(target_word, text):
    target_word = target_word.lower()
    return target_word in text_to_word_set(text)

if __name__ == '__main__':
    sample_text1 = "This is a sample text about python programming."
    sample_text2 = "This text does not contain the word python."
    sample_text3 = "Python is fun."
    sample_text4 = "programming"

    print(f"'{TARGET_WORD}' in '{sample_text1}': {word_present(TARGET_WORD, sample_text1)}")
    print(f"'{TARGET_WORD}' in '{sample_text2}': {word_present(TARGET_WORD, sample_text2)}")
    print(f"'{TARGET_WORD}' in '{sample_text3}': {word_present(TARGET_WORD, sample_text3)}")
    print(f"'{TARGET_WORD}' in '{sample_text4}': {word_present(TARGET_WORD, sample_text4)}")