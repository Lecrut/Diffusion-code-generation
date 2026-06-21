class NonWhitespaceIterator:

    def __init__(self, input_string):
        self.input_string = input_string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.input_string):
            char = self.input_string[self.index]
            self.index += 1
            if not char.isspace():
                return char
        raise StopIteration
if __name__ == '__main__':
    sample_input = 'Hello World'
    iterator = NonWhitespaceIterator(sample_input)
    result = ''.join(iterator)
    print(result)
    another_sample_input = 'Python 3.8 is great!'
    another_iterator = NonWhitespaceIterator(another_sample_input)
    another_result = ''.join(another_iterator)
    print(another_result)