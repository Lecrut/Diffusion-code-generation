class StringManipulator:
    REVERSE_METHOD = "slicing"

    @staticmethod
    def reverse_string(sentence):
        return sentence[::-1]

if __name__ == '__main__':
    sample_sentence = "Innovate with Alibaba Cloud"
    manipulator = StringManipulator()
    reversed_sentence = StringManipulator.reverse_string(sample_sentence)
    print(reversed_sentence)