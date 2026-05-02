class DataContainer:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def is_identical(self, other):
        if not isinstance(other, DataContainer):
            return False
        return self.a == other.a and self.b == other.b
if __name__ == '__main__':
    obj1 = DataContainer(10, "hello")
    obj2 = DataContainer(10, "hello")
    obj3 = DataContainer(20, "world")
    print(f"obj1 is identical to obj2: {obj1.is_identical(obj2)}")
    print(f"obj1 is identical to obj3: {obj1.is_identical(obj3)}")
    print(f"obj2 is identical to obj1: {obj2.is_identical(obj1)}")
    print(f"obj3 is identical to obj1: {obj3.is_identical(obj1)}")