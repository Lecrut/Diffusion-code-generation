class SentenceReverser:
    def __init__(self, sentence):
        if not isinstance(sentence, str):
            raise ValueError("Input must be a string")
        self.sentence = sentence

    def reverse(self):
        return self.sentence[::-1]

if __name__ == '__main__':
    sample_sentences = [
        "Hello, World!",
        "Python is fun",
        "Alibaba Cloud"
    ]
    for original in sample_sentences:
        try:
            reverser = SentenceReverser(original)
            result = reverser.reverse()
            print(f"Original: {original}")
            print(f"Reversed: {result}")
        except ValueError as e:
            print(e)