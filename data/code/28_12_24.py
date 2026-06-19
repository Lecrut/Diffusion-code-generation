class SortableObject:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        return self.value > other_value
if __name__ == '__main__':
    obj1 = SortableObject(10)
    obj2 = SortableObject(5)
    print(obj1.is_greater_than(obj2.value))