class SortableValue:
    VALID_TYPES = (int, float)

    def __init__(self, value):
        if not isinstance(value, self.VALID_TYPES):
            raise ValueError(f'value must be an instance of {self.VALID_TYPES}')
        self.value = value

    @staticmethod
    def _validate_type(other_value):
        if not isinstance(other_value, SortableValue.VALID_TYPES):
            raise ValueError(f'other_value must be an int or float')

    def is_greater_than(self, other_value):
        self._validate_type(other_value)
        return self.value > other_value
if __name__ == '__main__':
    value1 = SortableValue(50)
    value2 = SortableValue(30)
    result = value1.is_greater_than(value2.value)
    print(result)
    try:
        invalid_value = 'not a number'
        result = value1.is_greater_than(invalid_value)
    except ValueError as e:
        print(e)