class AlphabeticSequenceFinder:
    def __init__(self):
        self.alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def is_alphabetic(self, char):
        return char in self.alphabet

    def find_sequences(self, text):
        sequences = []
        current_sequence = []

        for char in text:
            if self.is_alphabetic(char):
                current_sequence.append(char)
            else:
                if current_sequence:
                    sequences.append(''.join(current_sequence))
                    current_sequence = []

        if current_sequence:
            sequences.append(''.join(current_sequence))

        return sequences

if __name__ == '__main__':
    finder = AlphabeticSequenceFinder()
    sample_string = "Hello, world! This is a test... how are you?"
    result = finder.find_sequences(sample_string)
    print(result)