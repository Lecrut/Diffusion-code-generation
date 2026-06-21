class StringManipulator:
    DEFAULT_DELIMITER = ' '

    @staticmethod
    def split_and_reverse(sentence):
        words = sentence.split(StringManipulator.DEFAULT_DELIMITER)
        reversed_words = words[::-1]
        return reversed_words

if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_sentence = "Hello world this is a test"
    result = manipulator.split_and_reverse(sample_sentence)
    print(result)