class MiddleElementFinder:
    _VALID_TYPES = (list, tuple)
    _SLICE_STEP = 2

    @staticmethod
    def _validate_input(data):
        if not isinstance(data, MiddleElementFinder._VALID_TYPES):
            raise ValueError("Input must be a list or tuple")
        if len(data) == 0:
            raise ValueError("Input must not be empty")

    @staticmethod
    def _compute_middle_index(length):
        return length // 2

    @classmethod
    def find_middle_element(cls, data):
        cls._validate_input(data)
        length = len(data)
        index = cls._compute_middle_index(length)
        start = index
        end = index + 1
        return data[start:end][0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70]
    result = MiddleElementFinder.find_middle_element(sample_list)
    print(result)