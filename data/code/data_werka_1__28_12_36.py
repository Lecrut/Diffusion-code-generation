class ComparableValue:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        return self.value > other_value
if __name__ == '__main__':
    obj1 = ComparableValue(10)
    obj2 = ComparableValue(5)
    result = obj1.is_greater_than(obj2.value)
    print(result)
    obj3 = ComparableValue(3)
    result2 = obj2.is_greater_than(obj3.value)
    print(result2)