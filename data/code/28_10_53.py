class SortableValue:

    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Initial value must be an int or float')
        self.value = value

    def is_greater_than(self, other_value):
        if not isinstance(other_value, (int, float)):
            raise ValueError('other_value must be an int or float')
        return self.value > other_value
if __name__ == '__main__':
    try:
        value1 = SortableValue(75)
        value2 = SortableValue(60)
        print(value1.is_greater_than(value2.value))
        print(value2.is_greater_than(value1.value))
    except ValueError as e:
        print(e)
    try:
        value3 = SortableValue(45)
        invalid_value = 'not a number'
        print(value3.is_greater_than(invalid_value))
    except ValueError as e:
        print(e)