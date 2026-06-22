class StringProcessor:
    @staticmethod
    def calculate_length(text):
        return len(text)

if __name__ == '__main__':
    sample_string = 'Hello World'
    length = StringProcessor.calculate_length(sample_string)
    print(length)