class ListProcessor:
    MID_INDEX_OFFSET = 0
    DIVISOR = 2
    ZERO_BASED_START = 0

    @staticmethod
    def _get_length(seq):
        return len(seq)

    @staticmethod
    def _is_empty(length):
        return length == 0

    @staticmethod
    def _is_odd(length):
        return length % 2 != 0

    def __init__(self, data):
        self.data = data

    def get_middle_element(self):
        n = self._get_length(self.data)
        if self._is_empty(n):
            raise ValueError("Cannot find middle of empty list")
        if self._is_odd(n):
            idx = n // self.DIVISOR
            return self.data[idx]
        idx = (n // self.DIVISOR) - 1
        return self.data[idx]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60, 70]
    processor = ListProcessor(sample_data)
    result = processor.get_middle_element()
    print(result)