class SortableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        if not isinstance(other_value, (int, float)):
            raise ValueError('other_value must be an int or float')
        return self.value > other_value
if __name__ == '__main__':
    val1 = SortableValue(10)
    val2 = SortableValue(5)
    result = val1.is_greater_than(val2.value)
    print(result)
    try:
        result = val1.is_greater_than('string')
    except ValueError as e:
        print(e)