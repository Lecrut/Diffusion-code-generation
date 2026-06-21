class AlphabetExtractor:
    ALPHABET_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @staticmethod
    def is_alphabetic(char):
        return char in AlphabetExtractor.ALPHABET_CHARS

    @classmethod
    def find_all_sequences(cls, text):
        sequences = []
        current_sequence = ''
        for char in text:
            if cls.is_alphabetic(char):
                current_sequence += char
            elif current_sequence:
                sequences.append(current_sequence)
                current_sequence = ''
        if current_sequence:
            sequences.append(current_sequence)
        return sequences
if __name__ == '__main__':
    sample_string = 'Hello, world! This is a test... how are you?'
    result = AlphabetExtractor.find_all_sequences(sample_string)
    print(result)