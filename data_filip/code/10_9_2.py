def reverse_words(sentence):
    words = []
    current_word = []
    for char in sentence:
        if char.isspace():
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        else:
            current_word.append(char)
    if current_word:
        words.append(''.join(current_word))
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_sentences = [
        "Hello World",
        "Python is fun",
        "One word",
        "  Multiple   spaces  between  words  ",
        "",
        "NoSpacesHere"
    ]
    for s in sample_sentences:
        print(reverse_words(s))