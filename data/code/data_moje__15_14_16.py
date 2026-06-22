class SequenceAccessor:
    def __init__(self, sequence):
        self._sequence = sequence

    def retrieve_second_to_last(self):
        if not hasattr(self._sequence, "__len__"):
            raise TypeError("Provided object is not a sequence")
        length = len(self._sequence)
        if length < 2:
            raise IndexError("Sequence must contain at least two elements")
        return self._sequence[length - 2]

if __name__ == '__main__':
    data = [100, 200, 300, 400, 500]
    accessor = SequenceAccessor(data)
    print(accessor.retrieve_second_to_last())
    short_data = [99]
    try:
        print(SequenceAccessor(short_data).retrieve_second_to_last())
    except IndexError as error:
        print(error)
    text_data = "hello"
    print(SequenceAccessor(text_data).retrieve_second_to_last())