class SortableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        if not isinstance(other_value, (int, float)):
            raise ValueError('other_value must be an int or float')
        return self.value > other_value
if __name__ == '__main__':
    try:
        value1 = SortableValue(30)
        value2 = SortableValue(20)
        result = value1.is_greater_than(value2.value)
        print(result)
    except ValueError as e:
        print(e)
    try:
        value3 = SortableValue(5)
        invalid_value = 'not a number'
        result = value3.is_greater_than(invalid_value)
        print(result)
    except ValueError as e:
        print(e)