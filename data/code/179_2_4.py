class WordReverser:
    def reverse_sentence(self, sentence: str) -> str:
        words = sentence.split()
        words.reverse()
        return " ".join(words)
if __name__ == '__main__':
    reverser = WordReverser()
    sample_sentence1 = "Hello world this is a test"
    result1 = reverser.reverse_sentence(sample_sentence1)
    print(f"Input: '{sample_sentence1}'")
    print(f"Output: '{result1}'")
    sample_sentence2 = "Efficient algorithm design"
    result2 = reverser.reverse_sentence(sample_sentence2)
    print(f"Input: '{sample_sentence2}'")
    print(f"Output: '{result2}'")
    sample_sentence3 = "a single word"
    result3 = reverser.reverse_sentence(sample_sentence3)
    print(f"Input: '{sample_sentence3}'")
    print(f"Output: '{result3}'")