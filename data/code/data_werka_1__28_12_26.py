class SortableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        return self.value > other_value
if __name__ == '__main__':
    value1 = SortableValue(10)
    value2 = SortableValue(5)
    print(value1.is_greater_than(value2))