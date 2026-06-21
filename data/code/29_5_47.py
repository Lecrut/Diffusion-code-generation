def validate_input(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    return word

def reverse_word(word):
    validated_word = validate_input(word)
    return validated_word[::-1]

class WordProcessor:
    def __init__(self, word):
        self.word = validate_input(word)

    def get_reversed(self):
        return self.word[::-1]

if __name__ == '__main__':
    sample_word = "hello"
    reversed_word_functional = reverse_word(sample_word)
    print(reversed_word_functional)

    processor = WordProcessor("world")
    reversed_word_class = processor.get_reversed()
    print(reversed_word_class)