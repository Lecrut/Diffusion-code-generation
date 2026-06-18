import string
def build_word_dictionary(filepath):
    word_set = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
            for char in text:
                if char.isalpha():
                    word_set.add(char)
    except FileNotFoundError:
        return word_set
    return word_set
if __name__ == '__main__':
    sample_filepath = "sample_text.txt"
    sample_content = "This is a sample text for building a dictionary. Words like python and script are important."
    with open(sample_filepath, 'w', encoding='utf-8') as f:
        f.write(sample_content)
    dictionary = build_word_dictionary(sample_filepath)
    print(dictionary)