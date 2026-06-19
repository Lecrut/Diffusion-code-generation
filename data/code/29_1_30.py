class StringManipulator:
    @staticmethod
    def reverse_word(word):
        return word[::-1]

if __name__ == '__main__':
    sample_string_1 = "world"
    reversed_string_1 = StringManipulator.reverse_word(sample_string_1)
    print(reversed_string_1)
    
    sample_string_2 = "Alibaba"
    reversed_string_2 = StringManipulator.reverse_word(sample_string_2)
    print(reversed_string_2)