class StringManipulator:
    _SLICE_START = slice(0, 1)
    _SLICE_END = slice(1, None)

    def __init__(self, data):
        self.data = data

    @staticmethod
    def _transform_char(char):
        return char.upper()

    @staticmethod
    def _join_sequence(sequence):
        return ''.join(sequence)

    def capitalize_first(self):
        if not self.data:
            return self.data
        head = self.data[self._SLICE_START]
        tail = self.data[self._SLICE_END]
        transformed_head = [self._transform_char(c) for c in head]
        return self._join_sequence(transformed_head + list(tail))

if __name__ == '__main__':
    inputs = ["python", "java", "c++", ""]
    processor = StringManipulator(inputs)
    result = processor.capitalize_first()
    print(result)