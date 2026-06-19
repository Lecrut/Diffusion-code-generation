class SortableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        return self.value > other_value
if __name__ == '__main__':
    value1 = SortableValue(10)
    value2 = SortableValue(5)
    result = value1.is_greater_than(value2.value)
    print(result)
    value3 = SortableValue(3)
    result2 = value1.is_greater_than(value3.value)
    print(result2)