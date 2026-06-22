class WordReverser:
    def __init__(self):
        self.sample_strings = {
            "sample1": "hello",
            "sample2": "world",
            "sample3": "Python",
            "sample4": "racecar"
        }

    def reverse_words(self, text):
        words = text.split()
        reversed_sentence = ' '.join(words[::-1])
        return reversed_sentence

if __name__ == '__main__':
    reverser = WordReverser()
    for key, value in reverser.sample_strings.items():
        original_string = value
        reversed_string = reverser.reverse_words(original_string)
        print(f"Original: {original_string}, Reversed: {reversed_string}")