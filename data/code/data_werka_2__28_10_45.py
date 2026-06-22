class SortableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        if not isinstance(other_value, (int, float)):
            raise ValueError('other_value must be an int or float')
        return self.value > other_value
if __name__ == '__main__':
    VALUE_THRESHOLD = 10
    value1 = SortableValue(35)
    value2 = SortableValue(VALUE_THRESHOLD)
    result = value1.is_greater_than(value2.value)
    print(f'Is value1 greater than value2? {result}')
    try:
        invalid_value = 'not a number'
        result = value1.is_greater_than(invalid_value)
        print(result)
    except ValueError as e:
        print(e)