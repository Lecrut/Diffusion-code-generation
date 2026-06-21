class ListAnalyzer:
    _VALID_TYPES = (list, tuple)
    _EMPTY_MSG = "List must not be empty"
    _TYPE_MSG = "Input must be a list or tuple"

    def __init__(self, data):
        if not isinstance(data, self._VALID_TYPES):
            raise ValueError(self._TYPE_MSG)
        if len(data) == 0:
            raise ValueError(self._EMPTY_MSG)
        self._elements = list(data)

    def get_middle_value(self):
        count = len(self._elements)
        if count % 2 == 1:
            return self._elements[count // 2]
        mid_right = count // 2
        mid_left = mid_right - 1
        return (self._elements[mid_left] + self._elements[mid_right]) / 2

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60]
    analyzer = ListAnalyzer(sample_list)
    result = analyzer.get_middle_value()
    print(result)
    sample_tuple = (1, 2, 3)
    analyzer2 = ListAnalyzer(sample_tuple)
    print(analyzer2.get_middle_value())