class SequenceAccessor:
    EMPTY_SEQUENCE_ERROR = "Sequence must not be empty"
    INVALID_TYPE_ERROR = "Input must be a sequence"

    @staticmethod
    def validate_input(data):
        if not isinstance(data, (list, tuple, str)):
            raise TypeError(SequenceAccessor.INVALID_TYPE_ERROR)
        if len(data) == 0:
            raise ValueError(SequenceAccessor.EMPTY_SEQUENCE_ERROR)

    @staticmethod
    def fetch_last(data):
        SequenceAccessor.validate_input(data)
        return data[-1]

if __name__ == '__main__':
    integers = [100, 200, 300, 400, 500]
    last_int = SequenceAccessor.fetch_last(integers)
    print(last_int)
    text = "Python3"
    last_char = SequenceAccessor.fetch_last(text)
    print(last_char)
    items = (True, False, True)
    last_bool = SequenceAccessor.fetch_last(items)
    print(last_bool)