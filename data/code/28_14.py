class Sortable:
    def __init__(self, value):
        self._value = value
    def is_greater_than(self, other_value):
        return self._value > other_value
if __name__ == '__main__':
    obj1 = Sortable(10)
    obj2 = Sortable(5)
    obj3 = Sortable(10)
    print(f"obj1 (10) is greater than obj2 (5): {obj1.is_greater_than(5)}")
    print(f"obj2 (5) is greater than obj1 (10): {obj2.is_greater_than(10)}")
    print(f"obj1 (10) is greater than obj3 (10): {obj1.is_greater_than(10)}")
    print(f"obj3 (10) is greater than obj1 (10): {obj3.is_greater_than(10)}")
    print(f"obj2 (5) is greater than obj3 (10): {obj2.is_greater_than(10)}")