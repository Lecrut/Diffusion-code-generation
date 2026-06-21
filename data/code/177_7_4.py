class StringProcessor:
    def split_string(self, input_string):
        return input_string.split()

if __name__ == '__main__':
    processor = StringProcessor()
    sample_string = 'Python is awesome'
    words = processor.split_string(sample_string)
    print(words)