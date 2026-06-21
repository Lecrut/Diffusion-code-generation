def convert_to_set(text):
    return set(text.split())

def word_present(target_word, text_set):
    return target_word in text_set

if __name__ == '__main__':
    target = "python"
    text1 = "This is a sample text about python programming."
    text2 = "This text does not contain the word python."
    text3 = "Python is fun."
    text4 = "programming"

    set_text1 = convert_to_set(text1)
    print(f"'{target}' in '{text1}': {word_present(target, set_text1)}")

    set_text2 = convert_to_set(text2)
    print(f"'{target}' in '{text2}': {word_present(target, set_text2)}")

    set_text3 = convert_to_set(text3)
    print(f"'{target}' in '{text3}': {word_present(target, set_text3)}")

    set_text4 = convert_to_set(text4)
    print(f"'{target}' in '{text4}': {word_present(target, set_text4)}")