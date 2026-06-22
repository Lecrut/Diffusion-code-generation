class SentenceReverser:
    def __init__(self, sentence):
        self.sentence = sentence

    def reverse_sentence(self):
        words = self.sentence.split()
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        return ' '.join(words)

if __name__ == '__main__':
    test_sentence = 'Hello world this is a test'
    reverser = SentenceReverser(test_sentence)
    reversed_sentence = reverser.reverse_sentence()
    print(reversed_sentence)