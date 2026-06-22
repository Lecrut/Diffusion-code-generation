class StringReverser:
    @staticmethod
    def reverse(s):
        return s[::-1]

if __name__ == '__main__':
    sample_string = "hello"
    reversed_string = StringReverser.reverse(sample_string)
    print(f"Original: {sample_string}, Reversed: {reversed_string}")