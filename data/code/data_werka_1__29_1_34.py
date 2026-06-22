class StringManipulator:
    @staticmethod
    def reverse_word(word):
        return word[::-1]

if __name__ == '__main__':
    sample_string = "hello"
    reversed_string = StringManipulator.reverse_word(sample_string)
    print(reversed_string)
    sample_string_2 = "Python"
    reversed_string_2 = StringManipulator.reverse_word(sample_string_2)
    print(reversed_string_2)