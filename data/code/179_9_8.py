def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def reverse_words_iterative(text):
    validate_input(text)
    words = text.split()
    reversed_words = []
    for word in reversed(words):
        reversed_words.append(word)
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_text = "Hello world from Python"
    print(reverse_words_iterative(sample_text))