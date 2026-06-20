class StringProcessor:
    @staticmethod
    def get_first_last(s):
        return s[0], s[-1]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    first_char, last_char = StringProcessor.get_first_last(sample_string)
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")