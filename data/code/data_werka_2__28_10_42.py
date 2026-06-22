class SortableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        if not isinstance(other_value, (int, float)):
            raise ValueError('other_value must be an int or float')
        return self.value > other_value
if __name__ == '__main__':
    try:
        value1 = SortableValue(35)
        value2 = SortableValue(28)
        result = value1.is_greater_than(value2.value)
        print(result)
    except ValueError as e:
        print(e)
    try:
        invalid_value = 'a string'
        result = value1.is_greater_than(invalid_value)
    except ValueError as e:
        print(e)
    value3 = SortableValue(40)
    print(value2.is_greater_than(value3.value))