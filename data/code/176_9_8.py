class StringProcessor:

    @staticmethod
    def is_letter(char):
        return char.isalpha()

    @classmethod
    def extract_letter_sequences(cls, text):
        sequences = []
        current_sequence = ''
        for char in text:
            if cls.is_letter(char):
                current_sequence += char
            elif current_sequence:
                sequences.append(current_sequence)
                current_sequence = ''
        if current_sequence:
            sequences.append(current_sequence)
        return sequences
if __name__ == '__main__':
    sample_text = 'Hello, World! 123 Python 3.8'
    processor = StringProcessor()
    letter_sequences = processor.extract_letter_sequences(sample_text)
    print(letter_sequences)