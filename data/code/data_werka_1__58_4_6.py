class ListProcessor:
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_iterable(cls, iterable):
        if not hasattr(iterable, '__iter__'):
            raise ValueError("Provided data is not an iterable")
        return cls(list(iterable))

    def get_first_element(self):
        if not self.data:
            raise IndexError("List is empty")
        return self.data[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    processor = ListProcessor.from_iterable(sample_list)
    first_element = processor.get_first_element()
    print(first_element)