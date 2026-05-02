class DataContainer:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def is_identical(self, other):
        if not isinstance(other, DataContainer):
            return False
        return self.a == other.a and self.b == other.b
if __name__ == '__main__':
    instance1 = DataContainer(10, "hello")
    instance2 = DataContainer(10, "hello")
    instance3 = DataContainer(20, "world")
    print(f"instance1 is identical to instance2: {instance1.is_identical(instance2)}")
    print(f"instance1 is identical to instance3: {instance1.is_identical(instance3)}")
    instance4 = DataContainer(10, "hello")
    print(f"instance1 is identical to instance4: {instance1.is_identical(instance4)}")