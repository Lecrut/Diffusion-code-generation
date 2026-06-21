class WordReverser:
    @staticmethod
    def reverse_words(input_string):
        words = input_string.split()
        return " ".join(reversed(words))

if __name__ == '__main__':
    sample_input1 = "  Hello world   this is a test "
    sample_input2 = "singleword"
    sample_input3 = "   multiple   spaces   here"
    
    print(f"Input: '{sample_input1}'")
    print("Output:", WordReverser.reverse_words(sample_input1))
    print("-" * 20)
    print(f"Input: '{sample_input2}'")
    print("Output:", WordReverser.reverse_words(sample_input2))
    print("-" * 20)
    print(f"Input: '{sample_input3}'")