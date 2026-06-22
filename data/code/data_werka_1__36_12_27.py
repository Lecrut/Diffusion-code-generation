class WordReverser:
    def reverse_words(self, sentence):
        if not isinstance(sentence, str):
            raise ValueError("Input must be a string")
        
        words = sentence.split()
        reversed_sentence = ' '.join(words[::-1])
        return reversed_sentence

if __name__ == '__main__':
    try:
        reverser = WordReverser()
        sample_sentences = [
            "Hello world this is a test",
            "Python programming is fun",
            "Reverse these words please",
            "Keep it simple and efficient"
        ]
        
        for sentence in sample_sentences:
            reversed_sentence = reverser.reverse_words(sentence)
            print(f"Original: {sentence}, Reversed: {reversed_sentence}")
    except ValueError as e:
        print(e)