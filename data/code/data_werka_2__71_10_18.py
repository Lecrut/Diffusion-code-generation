class MiddleElementFinder:
    _HALF = 0.5

    @staticmethod
    def _validate_sequence(data):
        if not hasattr(data, '__len__'):
            raise ValueError("Input must be a sequence")
        if len(data) == 0:
            raise ValueError("Sequence must not be empty")
        return data

    @staticmethod
    def _get_odd_middle(data):
        length = len(data)
        mid_index = length // 2
        return data[mid_index]

    @staticmethod
    def _get_even_middle(data):
        length = len(data)
        mid_index = length // 2
        left_val = data[mid_index - 1]
        right_val = data[mid_index]
        return (left_val + right_val) * MiddleElementFinder._HALF

    def find_middle(self, data):
        validated_data = self._validate_sequence(data)
        length = len(validated_data)
        if length % 2 == 1:
            return self._get_odd_middle(validated_data)
        return self._get_even_middle(validated_data)

if __name__ == '__main__':
    finder = MiddleElementFinder()
    odd_list = [1, 3, 5, 7, 9]
    even_list = [2, 4, 6, 8]
    print(finder.find_middle(odd_list))
    print(finder.find_middle(even_list))