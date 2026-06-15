class StringProcessor:
    def extract_alphabetic_sequences(self, text):
        result = []
        current_sequence = ""
        for char in text:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                current_sequence += char
            else:
                if current_sequence:
                    result.append(current_sequence)
                current_sequence = ""
        if current_sequence:
            result.append(current_sequence)
        return result
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string1 = "Hello World! 123 Python is fun."
    sample_string2 = "A-bC dEfG!hIj"
    sample_string3 = "NoAlphanumericCharactersHere"
    sample_string4 = "spaces and symbols only"
    print(f"'{sample_string1}' -> {processor.extract_alphabetic_sequences(sample_string1)}")
    print(f"'{sample_string2}' -> {processor.extract_alphabetic_sequences(sample_string2)}")
    print(f"'{sample_string3}' -> {processor.extract_alphabetic_sequences(sample_string3)}")
    print(f"'{sample_string4}' -> {processor.extract_alphabetic_sequences(sample_string4)}")