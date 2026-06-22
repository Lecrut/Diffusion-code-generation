class StringReverser:
    @staticmethod
    def reverse(s):
        return s[::-1]

if __name__ == '__main__':
    sample_input = "Alibaba Cloud"
    print(StringReverser.reverse(sample_input))