class StringUtils:
    @staticmethod
    def calculate_length(s):
        return len(s)

if __name__ == '__main__':
    sample_string = "Hello, World!"
    length = StringUtils.calculate_length(sample_string)
    print(length)