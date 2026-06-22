class SortableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        return self.value > other_value
if __name__ == '__main__':
    obj1 = SortableValue(10)
    obj2 = SortableValue(5)
    result = obj1.is_greater_than(obj2.value)
    print(result)
    obj3 = SortableValue(7)
    result2 = obj3.is_greater_than(obj1.value)
    print(result2)