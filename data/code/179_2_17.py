class SentenceReverser:

    def reverse_words(self, sentence: str) -> str:
        words = sentence.split()
        words.reverse()
        return ' '.join(words)
if __name__ == '__main__':
    reverser = SentenceReverser()
    sample_sentence1 = 'Hello world this is a test'
    result1 = reverser.reverse_words(sample_sentence1)
    print(f'Original: {sample_sentence1}')
    print(f'Reversed: {result1}')
    sample_sentence2 = 'Optimization is key for efficiency'
    result2 = reverser.reverse_words(sample_sentence2)
    print(f'Original: {sample_sentence2}')
    print(f'Reversed: {result2}')
    sample_sentence3 = '  leading and trailing spaces  '
    result3 = reverser.reverse_words(sample_sentence3)
    print(f"Original: '{sample_sentence3}'")
    print(f"Reversed: '{result3.strip()}'")