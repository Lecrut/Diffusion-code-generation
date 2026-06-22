class ListAnalyzer:
    _EMPTY_RESULT = None
    _ODD_INDEX_OFFSET = 0
    _EVEN_INDEX_OFFSET = 1

    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Input must be a list")
        if len(data) == 0:
            raise ValueError("List cannot be empty")
        self.data = data

    def get_middle_value(self):
        length = len(self.data)
        if length % 2 == 1:
            index = length // 2
            return self.data[index]
        index = length // 2
        val1 = self.data[index - self._EVEN_INDEX_OFFSET]
        val2 = self.data[index]
        return (val1 + val2) / 2

if __name__ == '__main__':
    analyzer1 = ListAnalyzer([1, 2, 3, 4, 5])
    print(analyzer1.get_middle_value())
    analyzer2 = ListAnalyzer([10, 20, 30, 40])
    print(analyzer2.get_middle_value())
    analyzer3 = ListAnalyzer([7])
    print(analyzer3.get_middle_value())