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
    value3 = 'a'
    print(value1.is_greater_than(value2))
    try:
        print(value1.is_greater_than(value3))
    except ValueError as e:
        print(e)