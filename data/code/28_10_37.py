class SortableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        if not isinstance(other_value, (int, float)):
            raise ValueError('other_value must be an int or float')
        return self.value > other_value
if __name__ == '__main__':
    value1 = SortableValue(25)
    value2 = SortableValue(15)
    result = value1.is_greater_than(value2.value)
    print(result)
    try:
        result = value1.is_greater_than('a string')
    except ValueError as e:
        print(e)