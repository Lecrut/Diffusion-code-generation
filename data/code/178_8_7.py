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
    sample_string1 = "Hello World! 123 abcdef and more."
    sample_string2 = "Python is fun, how are you?"
    sample_string3 = "A B C-D E F G"
    sample_string4 = "NoLettersHere"
    print(f"Input: '{sample_string1}'")
    print(f"Output: {processor.extract_alphabetic_sequences(sample_string1)}")
    print("-" * 20)
    print(f"Input: '{sample_string2}'")
    print(f"Output: {processor.extract_alphabetic_sequences(sample_string2)}")
    print("-" * 20)
    print(f"Input: '{sample_string3}'")
    print(f"Output: {processor.extract_alphabetic_sequences(sample_string3)}")
    print("-" * 20)
    print(f"Input: '{sample_string4}'")
    print(f"Output: {processor.extract_alphabetic_sequences(sample_string4)}")