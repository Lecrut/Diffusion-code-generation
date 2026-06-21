class StringReverser:
    @staticmethod
    def reverse(s):
        return ''.join(reversed(s))

if __name__ == '__main__':
    sample_string = "Alibaba"
    print(StringReverser.reverse(sample_string))