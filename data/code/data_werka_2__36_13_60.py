class SentenceReverser:
    def __init__(self, sentence):
        self.sentence = list(sentence)
    
    def reverse_sentence(self):
        self._reverse_range(0, len(self.sentence) - 1)
        start = 0
        for end in range(len(self.sentence)):
            if self.sentence[end] == ' ':
                self._reverse_range(start, end - 1)
                start = end + 1
        self._reverse_range(start, len(self.sentence) - 1)
    
    def _reverse_range(self, start, end):
        while start < end:
            self.sentence[start], self.sentence[end] = self.sentence[end], self.sentence[start]
            start += 1
            end -= 1
    
    def get_reversed_sentence(self):
        return ''.join(self.sentence)

if __name__ == '__main__':
    test_cases = [
        'Hello World',
        'Python is fun',
        'Reverse this sentence',
        'A quick brown fox',
        'Keep it simple'
    ]
    
    for sentence in test_cases:
        reverser = SentenceReverser(sentence)
        reverser.reverse_sentence()
        print(reverser.get_reversed_sentence())