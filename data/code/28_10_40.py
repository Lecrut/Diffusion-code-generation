class SortableValue:

    def __init__(self, value):
        self.value = value

    def _validate_other_value(self, other_value):
        if not isinstance(other_value, (int, float)):
            raise ValueError('other_value must be an int or float')

    def is_greater_than(self, other_value):
        self._validate_other_value(other_value)
        return self.value > other_value
if __name__ == '__main__':
    value1 = SortableValue(50)
    value2 = SortableValue(30)
    result = value1.is_greater_than(value2.value)
    print(result)
    try:
        invalid_result = value1.is_greater_than('a string')
    except ValueError as e:
        print(e)