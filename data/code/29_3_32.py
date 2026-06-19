class StringReverser:
    @staticmethod
    def reverse(s: str) -> str:
        return s[::-1]

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    reversed_string = StringReverser.reverse(sample_string)
    print(reversed_string)