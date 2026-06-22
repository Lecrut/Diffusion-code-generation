class ListProcessor:

    def __init__(self, data):
        self.data = data

    @classmethod
    def from_iterable(cls, iterable):
        if not hasattr(iterable, '__iter__'):
            raise ValueError('Provided input is not an iterable')
        return cls(list(iterable))

    def get_first_element(self):
        if not self.data:
            return None
        return self.data[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    processor = ListProcessor(sample_list)
    first_element = processor.get_first_element()
    print(first_element)
    try:
        string_processor = ListProcessor.from_iterable('hello world')
        first_char = string_processor.get_first_element()
        print(first_char)
    except ValueError as e:
        print(e)