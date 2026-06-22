class ListChecker:
    def __init__(self):
        self._min_length = 1

    def _validate_input(self, data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input must be a sequence type")
        if len(data) < self._min_length:
            raise ValueError("Input sequence must contain at least one element")
        return data

    def get_extremes(self, data):
        validated_data = self._validate_input(data)
        first_element = validated_data[0]
        last_element = validated_data[-1]
        return (first_element, last_element)

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    checker = ListChecker()
    result = checker.get_extremes(sample_data)
    print(result)