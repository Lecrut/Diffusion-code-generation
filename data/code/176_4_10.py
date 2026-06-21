class AlphaSequenceFinder:
    def __init__(self):
        self.alphabetic_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def is_alphabetic(self, char):
        return char in self.alphabetic_chars

    def find_sequences(self, text):
        sequences = []
        current_sequence = []

        for char in text:
            if self.is_alphabetic(char):
                current_sequence.append(char)
            elif current_sequence:
                sequences.append(''.join(current_sequence))
                current_sequence = []

        if current_sequence:
            sequences.append(''.join(current_sequence))

        return sequences

if __name__ == '__main__':
    finder = AlphaSequenceFinder()
    sample_string = "Hello, world! This is a test... how are you?"
    result = finder.find_sequences(sample_string)
    print(result)