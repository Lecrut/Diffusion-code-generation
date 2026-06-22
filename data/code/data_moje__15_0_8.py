class SequenceAccessor:
    def __init__(self, sequence):
        self._sequence = sequence

    def get_second_to_last(self):
        if not isinstance(self._sequence, (list, tuple)):
            raise TypeError("Input must be a list or tuple")
        length = len(self._sequence)
        if length < 2:
            raise IndexError("Sequence must contain at least two elements to retrieve the second-to-last element")
        return self._sequence[-2]

if __name__ == '__main__':
    test_data = [5, 12, 88, 3, 99]
    accessor = SequenceAccessor(test_data)
    print(accessor.get_second_to_last())
    short_data = [42]
    try:
        short_accessor = SequenceAccessor(short_data)
        short_accessor.get_second_to_last()
    except IndexError as e:
        print(e)