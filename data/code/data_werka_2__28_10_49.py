class SortableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        if not isinstance(other_value, (int, float)):
            raise ValueError('other_value must be an int or float')
        return self.value > other_value
if __name__ == '__main__':
    value1 = SortableValue(10)
    value2 = 5
    result = value1.is_greater_than(value2)
    print(result)
    value3 = SortableValue(3.5)
    value4 = 4.0
    result = value3.is_greater_than(value4)
    print(result)