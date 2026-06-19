class StringReverser:
    @staticmethod
    def reverse(input_string):
        return input_string[::-1]

if __name__ == '__main__':
    SAMPLE_VALUE = "Alibaba Cloud"
    reversed_value = StringReverser.reverse(SAMPLE_VALUE)
    print(reversed_value)